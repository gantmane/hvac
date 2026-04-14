#!/usr/bin/env python3
"""Translate 52 English titles in content-ru to Russian."""
import re
from pathlib import Path

ROOT = Path("/Users/evgenygantman/Documents/github/gantmane/hvac/content-ru")

TITLE_MAP = {
    "80 Percent RH Threshold": "Порог относительной влажности 80%",
    "Air Conditioning Considerations": "Особенности кондиционирования воздуха",
    "Air Impermeable Materials": "Воздухонепроницаемые материалы",
    "Air Permeable Materials": "Воздухопроницаемые материалы",
    "Allium": "Луковые культуры",
    "Antoine Equation": "Уравнение Антуана",
    "Azeotropic Mixtures": "Азеотропные смеси",
    "Balanced Drying": "Сбалансированное высыхание",
    "Biohygrothermal Models": "Биогигротермические модели",
    "Capillary Breaks": "Капиллярные разрывы",
    "Cold Climate Assemblies": "Ограждающие конструкции для холодного климата",
    "Construction": "Построение",
    "Definition and Fundamental Concepts": "Определение и основные понятия",
    "Dominance Over Diffusion": "Доминирование над диффузией",
    "E. coli": "Escherichia coli",
    "Equations Of State": "Уравнения состояния",
    "Extended Surfaces": "Развитые поверхности (рёбра)",
    "External Flow": "Внешнее обтекание",
    "Fick's Law of Diffusion": "Закон диффузии Фика",
    "Foam Boards": "Пенопластовые плиты",
    "Fundamentals": "Основы",
    "Hot-Humid Climate Assemblies": "Ограждающие конструкции для жаркого влажного климата",
    "Internal Flow": "Внутреннее течение",
    "Isenthalps": "Изоэнтальпы",
    "Isentropes": "Изоэнтропы",
    "Isopleth Systems": "Изоплетные системы",
    "Isotherms": "Изотермы",
    "Materials Comparison": "Сравнение материалов",
    "Metals": "Металлы",
    "Mixed Climate Strategies": "Стратегии для смешанного климата",
    "Moisture Control": "Контроль влажности",
    "Quality Lines": "Линии паросодержания",
    "R1234yf Tables": "Таблицы R1234yf",
    "R1234ze Tables": "Таблицы R1234ze",
    "R134a Tables": "Таблицы R134a",
    "R32 Tables": "Таблицы R32",
    "R410a Tables": "Таблицы R410a",
    "R452b Tables": "Таблицы R452b",
    "R454b Tables": "Таблицы R454b",
    "R513a Tables": "Таблицы R513a",
    "R515b Tables": "Таблицы R515b",
    "R744 CO2 Tables": "Таблицы R744 (CO₂)",
    "Rainscreen Systems": "Системы вентилируемого фасада",
    "Semi Permeable Assemblies": "Полупроницаемые ограждающие конструкции",
    "Temperature Control": "Контроль температуры",
    "Temperature Requirements": "Температурные требования",
    "Testing Methods": "Методы испытаний",
    "Time Duration": "Продолжительность воздействия",
    "VTT Model": "Модель VTT",
    "Ventilation": "Вентиляция",
    "Water Activity": "Активность воды",
    "Zeotropic Mixtures": "Зеотропные смеси",
}

TITLE_RE = re.compile(r'^(title:\s*)("?)([^\n"]*?)("?)\s*$', re.MULTILINE)

fixed = 0
skipped = 0
with open(Path(__file__).parent / "wave3-entitle-safe.txt") as f:
    paths = [line.strip() for line in f if line.strip()]

for rel in paths:
    p = ROOT / rel
    text = p.read_text(encoding="utf-8")
    m = TITLE_RE.search(text)
    if not m:
        skipped += 1
        continue
    current = m.group(3).strip()
    if current not in TITLE_MAP:
        skipped += 1
        print(f"SKIP {rel}: title={current!r}")
        continue
    new_title = TITLE_MAP[current]
    # Always quote Russian titles
    new_line = f'title: "{new_title}"'
    new_text = text[:m.start()] + new_line + text[m.end():]
    p.write_text(new_text, encoding="utf-8")
    fixed += 1

print(f"fixed={fixed} skipped={skipped}")
