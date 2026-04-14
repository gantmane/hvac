#!/usr/bin/env python3
"""Generate substantive Russian HVAC content for thin leaf pages.
Uses Sonnet 4.6 via the same OAuth auth as batch_translate_claude.py.
Preserves frontmatter, replaces body with a comprehensive technical article.
"""
import os, sys, re, time, json, threading
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, '/Users/evgenygantman/Documents/github/gantmane/hvac')
from batch_translate_claude import get_oauth_token, strip_preamble, log, append_state

ROOT = Path('/Users/evgenygantman/Documents/github/gantmane/hvac/content-ru')
LIST = Path(os.environ.get('WAVE_LIST', '/Users/evgenygantman/Documents/github/gantmane/hvac/__in/thin-leaves.txt'))
LIMIT = int(os.environ.get('WAVE_LIMIT', '100'))
MODEL = 'claude-haiku-4-5-20251001'
MAX_WORKERS = 10
MAX_TOKENS = 12000
MAX_RETRIES = 3

SYSTEM = """Вы — эксперт по проектированию систем ОВК (HVAC), пишущий справочный материал
для профессиональной русскоязычной технической энциклопедии. Ваш стиль — строгий,
инженерный, со ссылками на стандарты ASHRAE, ISO, EN, ГОСТ где это уместно.

ЗАДАЧА: по краткому заглушечному описанию страницы (заголовок, иерархия раздела,
существующий список подтем) напишите полноценную техническую статью 300–500 строк
на русском языке в формате Markdown.

ОБЯЗАТЕЛЬНЫЕ ТРЕБОВАНИЯ:
1. Используйте метрическую систему (СИ): °C, Па, кПа, м³/ч, Вт/м·К, кДж/кг, кг/м³, м/с.
2. Сохраните акронимы на английском: HVAC, ASHRAE, SEER, COP, EER, VAV, CAV, CFM,
   AHRI, EPA, ISO, ANSI, NFPA, LEED, BREEAM, PM2.5, VOC, R-134a и т. п.
3. Структура статьи:
   ## Обзор (2–4 абзаца: определение, значимость, область применения)
   ## Физические принципы / Теоретические основы (уравнения, явления, механизмы)
   ## Компоненты и конструкция (подробное описание каждой подтемы из заглушки)
   ## Методы расчёта / Методика проектирования (формулы с расшифровкой переменных)
   ## Применение в ОВК (конкретные сценарии, типы систем, климатические зоны)
   ## Стандарты и нормативы (ASHRAE, ISO, ГОСТ, СП, СНиП)
   ## Практические рекомендации (значения по умолчанию, типовые диапазоны, ошибки)
4. Включайте численные примеры и типовые диапазоны значений с единицами СИ.
5. Используйте таблицы для сводных данных (свойств, диапазонов, классов).
6. Формулы пишите в LaTeX-нотации: $Q = m \\cdot c \\cdot \\Delta T$, $$\\Delta P = \\rho g h$$.
7. НЕ добавляйте вводных фраз («Вот статья»), НЕ оборачивайте в тройные бэктики.
8. Начните ответ СРАЗУ с frontmatter YAML (--- ... ---), затем тело статьи.
9. Сохраните существующий frontmatter (title, weight) без изменений, можете добавить
   description (1 предложение на русском).

НЕ выдумывайте несуществующие стандарты. Если не уверены в конкретном номере ГОСТ —
пишите обобщённо («действующие ГОСТ Р серии 30494»).
"""

_tls = threading.local()

def get_client():
    if not hasattr(_tls, 'client'):
        for var in ('ANTHROPIC_BASE_URL', 'ANTHROPIC_API_KEY'):
            os.environ.pop(var, None)
        import anthropic
        _tls.client = anthropic.Anthropic(
            auth_token=get_oauth_token(),
            default_headers={'anthropic-beta': 'oauth-2025-04-20'},
            max_retries=0,
        )
    return _tls.client


def parse_stub(text: str):
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
    if not m:
        return None, None, text
    fm = m.group(1)
    body = text[m.end():]
    title_m = re.search(r'^title:\s*"?([^\n"]+)"?\s*$', fm, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else '?'
    return fm, title, body


def build_prompt(rel: str, fm: str, title: str, body: str) -> str:
    breadcrumbs = ' > '.join(rel.replace('/_index.md','').replace('.md','').split('/'))
    return (
        f"Раздел (иерархия): {breadcrumbs}\n"
        f"Заголовок страницы: {title}\n\n"
        f"Существующий заглушечный контент (заменить на полноценную статью):\n"
        f"---\n{fm}\n---\n{body.strip()}\n\n"
        f"Напишите полноценную статью 300–500 строк на русском по данной теме. "
        f"Сохраните исходные поля frontmatter (title, weight), добавьте description."
    )


def generate(rel: str) -> tuple[str, bool, str, float]:
    t0 = time.time()
    p = ROOT / rel
    try:
        text = p.read_text(encoding='utf-8')
        fm, title, body = parse_stub(text)
        if fm is None:
            return rel, False, 'no-frontmatter', 0.0
        prompt = build_prompt(rel, fm, title, body)
        client = get_client()
        last = None
        for attempt in range(MAX_RETRIES):
            try:
                parts = []
                with client.messages.stream(
                    model=MODEL,
                    max_tokens=MAX_TOKENS,
                    system=SYSTEM,
                    messages=[{"role": "user", "content": prompt}],
                ) as stream:
                    for chunk in stream.text_stream:
                        parts.append(chunk)
                out = strip_preamble(''.join(parts)).strip()
                # If model omitted frontmatter, prepend the original one.
                if not out.startswith('---'):
                    out = f"---\n{fm}\n---\n\n{out}"
                else:
                    # Model emitted its own frontmatter — ensure original title/weight preserved.
                    m2 = re.match(r'^---\s*\n(.*?)\n---\s*\n', out, re.DOTALL)
                    if m2:
                        new_fm = m2.group(1)
                        # Force original title + weight back in if model changed them
                        for key in ('title', 'weight'):
                            orig_m = re.search(rf'^{key}:.*$', fm, re.MULTILINE)
                            if orig_m:
                                if re.search(rf'^{key}:.*$', new_fm, re.MULTILINE):
                                    new_fm = re.sub(rf'^{key}:.*$', orig_m.group(0), new_fm, flags=re.MULTILINE)
                                else:
                                    new_fm = orig_m.group(0) + '\n' + new_fm
                        out = f"---\n{new_fm}\n---\n{out[m2.end():]}"
                if len(out) < 1500:
                    raise RuntimeError(f'output too short ({len(out)}B)')
                p.write_text(out.rstrip() + '\n', encoding='utf-8')
                return rel, True, f'ok({len(text)}->{len(out)}B)', time.time()-t0
            except Exception as e:
                last = e
                msg = str(e)
                if '429' in msg or 'rate_limit' in msg:
                    time.sleep(60 + 30*attempt)
                else:
                    time.sleep(2**attempt)
        raise RuntimeError(f'failed after {MAX_RETRIES}: {last}')
    except Exception as e:
        return rel, False, str(e)[:200], time.time()-t0


def main():
    files = [l.strip() for l in LIST.read_text().splitlines() if l.strip()][:LIMIT]
    log(f"WAVE-C START: {len(files)} files, model={MODEL}, workers={MAX_WORKERS}")
    t0 = time.time()
    ok = fail = 0
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futs = {ex.submit(generate, f): f for f in files}
        for fut in as_completed(futs):
            rel, success, status, dt = fut.result()
            if success:
                ok += 1
                log(f"[{ok+fail}/{len(files)}] ok {rel} {status} ({dt:.1f}s)")
            else:
                fail += 1
                log(f"[{ok+fail}/{len(files)}] FAIL {rel}: {status}")
            append_state({"wave": "C", "file": rel, "status": "ok" if success else "fail",
                          "info": status, "duration": round(dt,1)})
    log(f"WAVE-C DONE: {ok} ok, {fail} fail in {(time.time()-t0)/60:.1f} min")


if __name__ == '__main__':
    main()
