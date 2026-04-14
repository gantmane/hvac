---
title: "Соотношения свойств и уравнения Максвелла"
aliases: ["Соотношения свойств и уравнения Максвелла"]
description: "Строгий вывод соотношений Максвелла из термодинамических потенциалов; уравнения Клапейрона и Клаузиуса–Клапейрона; соотношения для теплоёмкостей; уравнение Гиббса–Дюгема; применение к расчёту свойств хладагентов и построению таблиц термодинамических данных."
date: 2024-01-01
lastmod: 2026-04-15
author: "Evgeniy Gantman"
keywords:
  - соотношения Максвелла
  - термодинамические потенциалы
  - уравнение Клапейрона
  - Клаузиус Клапейрон
  - теплоёмкость
  - свободная энергия Гиббса
  - свободная энергия Гельмгольца
  - уравнения состояния хладагентов
categories:
  - Термодинамика
  - Соотношения свойств
tags:
  - Максвелл
  - термодинамические потенциалы
  - Клапейрон
  - свойства хладагентов
weight: 8
---

## Фундаментальные уравнения термодинамики

Основу для вывода всех соотношений свойств составляют **фундаментальные уравнения Гиббса** (Gibbs fundamental relations). Для закрытой системы с простым сжимаемым веществом:

{{< formula display="true" >}}
dU = T\,dS - P\,dV
{{< /formula >}}

Это уравнение содержит всю термодинамическую информацию о веществе: зная функцию U(S, V), можно получить все другие свойства.

---

## Четыре термодинамических потенциала

### Внутренняя энергия U(S, V)

{{< formula display="true" >}}
dU = T\,dS - P\,dV, \qquad T = \left(\frac{\partial U}{\partial S}\right)_V, \quad P = -\left(\frac{\partial U}{\partial V}\right)_S
{{< /formula >}}

### Энтальпия H(S, P)

Преобразование Лежандра: {{< formula >}}H = U + PV{{< /formula >}}

{{< formula display="true" >}}
dH = T\,dS + V\,dP, \qquad T = \left(\frac{\partial H}{\partial S}\right)_P, \quad V = \left(\frac{\partial H}{\partial P}\right)_S
{{< /formula >}}

### Свободная энергия Гельмгольца A(T, V)

{{< formula display="true" >}}
A = U - TS, \qquad dA = -S\,dT - P\,dV
{{< /formula >}}

{{< formula display="true" >}}
S = -\left(\frac{\partial A}{\partial T}\right)_V, \quad P = -\left(\frac{\partial A}{\partial V}\right)_T
{{< /formula >}}

Физический смысл: A — максимальная работа, которую может совершить система в изотермном процессе.

### Энергия Гиббса G(T, P)

{{< formula display="true" >}}
G = H - TS, \qquad dG = -S\,dT + V\,dP
{{< /formula >}}

{{< formula display="true" >}}
S = -\left(\frac{\partial G}{\partial T}\right)_P, \quad V = \left(\frac{\partial G}{\partial P}\right)_T
{{< /formula >}}

Физический смысл: G — максимальная полезная (не PV) работа в изотермно-изобарном процессе. Критерий фазового равновесия: при равновесии {{< formula >}}G_f = G_g{{< /formula >}}.

---

## Соотношения Максвелла

Из условия равенства смешанных вторых частных производных («перекрёстные производные» точных дифференциалов):

{{< formula display="true" >}}
\left(\frac{\partial T}{\partial V}\right)_S = -\left(\frac{\partial P}{\partial S}\right)_V \quad \text{(из }dU\text{)}
{{< /formula >}}

{{< formula display="true" >}}
\left(\frac{\partial T}{\partial P}\right)_S = \left(\frac{\partial V}{\partial S}\right)_P \quad \text{(из }dH\text{)}
{{< /formula >}}

{{< formula display="true" >}}
\left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial P}{\partial T}\right)_V \quad \text{(из }dA\text{)}
{{< /formula >}}

{{< formula display="true" >}}
\left(\frac{\partial S}{\partial P}\right)_T = -\left(\frac{\partial V}{\partial T}\right)_P \quad \text{(из }dG\text{)}
{{< /formula >}}

### Мнемоническое правило

Запомнить соотношения помогает схема «квадрат Максвелла» (Born square): на вершинах — U, H, A, G; на сторонах — переменные T, P, S, V; диагонали определяют знаки. Альтернативно, достаточно помнить фундаментальные уравнения и применять условие точности.

---

## Применение соотношений Максвелла

### Вычисление ∂S/∂P при постоянной T

Из четвёртого соотношения Максвелла:

{{< formula display="true" >}}
\left(\frac{\partial S}{\partial P}\right)_T = -\left(\frac{\partial V}{\partial T}\right)_P
{{< /formula >}}

Правая часть выражается через коэффициент объёмного расширения {{< formula >}}\beta = \frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_P{{< /formula >}}:

{{< formula display="true" >}}
\left(\frac{\partial S}{\partial P}\right)_T = -V\beta
{{< /formula >}}

Это соотношение позволяет вычислить изменение энтропии при изменении давления из P-v-T данных — без прямого измерения энтропии:

{{< formula display="true" >}}
s_2 - s_1 = -\int_{P_1}^{P_2} V\beta \, dP \bigg|_T
{{< /formula >}}

### Вычисление ∂h/∂P при постоянной T

{{< formula display="true" >}}
\left(\frac{\partial h}{\partial P}\right)_T = v - T\left(\frac{\partial v}{\partial T}\right)_P = v(1 - T\beta)
{{< /formula >}}

Для идеального газа: {{< formula >}}Pv = RT \Rightarrow \beta = 1/T \Rightarrow \left(\partial h/\partial P\right)_T = 0{{< /formula >}} — энтальпия идеального газа не зависит от давления.

Для реальных газов {{< formula >}}\left(\partial h/\partial P\right)_T \neq 0{{< /formula >}} — поправка важна при высоких давлениях.

---

## Уравнение Клапейрона

Уравнение Клапейрона (Clapeyron equation) описывает наклон кривой фазового равновесия на P–T диаграмме:

{{< formula display="true" >}}
\frac{dP_{sat}}{dT} = \frac{h_{fg}}{T \cdot v_{fg}} = \frac{s_{fg}}{v_{fg}}
{{< /formula >}}

**Вывод.** При фазовом равновесии {{< formula >}}G_f = G_g{{< /formula >}}. Дифференцируя: {{< formula >}}dG_f = dG_g{{< /formula >}}, т.е. {{< formula >}}-s_f\,dT + v_f\,dP = -s_g\,dT + v_g\,dP{{< /formula >}}. Отсюда:

{{< formula display="true" >}}
\frac{dP}{dT} = \frac{s_g - s_f}{v_g - v_f} = \frac{s_{fg}}{v_{fg}} = \frac{h_{fg}}{T v_{fg}}
{{< /formula >}}

Уравнение Клапейрона точно и применимо ко всем фазовым переходам (жидкость–пар, твёрдое–жидкость, твёрдое–пар).

### Числовой пример: кривая насыщения R-134a

При T = 303 К (30 °C) для R-134a: h_fg = 1130 кДж/кг, v_fg = v_g − v_f = 0,02634 − 0,000843 = 0,02550 м³/кг.

{{< formula display="true" >}}
\frac{dP_{sat}}{dT}\bigg|_{30°C} = \frac{1130}{303 \times 0{,}02550} = \frac{1130}{7{,}727} = 146 \text{ кПа/К}
{{< /formula >}}

Это означает: при подъёме температуры конденсации на 1 К давление насыщения растёт примерно на 146 кПа — важная характеристика для настройки защиты по высокому давлению.

---

## Уравнение Клаузиуса–Клапейрона

При давлениях существенно ниже критического ({{< formula >}}P \ll P_{cr}{{< /formula >}}) пар можно рассматривать как идеальный газ: {{< formula >}}v_g \approx RT/P{{< /formula >}} и {{< formula >}}v_g \gg v_f{{< /formula >}}, поэтому {{< formula >}}v_{fg} \approx RT/P{{< /formula >}}. Подставляя в уравнение Клапейрона:

{{< formula display="true" >}}
\frac{d\ln P_{sat}}{dT} = \frac{h_{fg}}{RT^2}
{{< /formula >}}

В предположении h_fg = const:

{{< formula display="true" >}}
\ln\frac{P_{sat,2}}{P_{sat,1}} = \frac{h_{fg}}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)
{{< /formula >}}

или

{{< formula display="true" >}}
P_{sat} = A \cdot \exp\left(-\frac{h_{fg}}{RT}\right)
{{< /formula >}}

**Применение**: быстрая оценка давления насыщения при изменении температуры; проверка таблиц свойств; аппроксимация кривых насыщения хладагентов при инженерных расчётах.

---

## Соотношения для теплоёмкостей

### Разность cp − cv

{{< formula display="true" >}}
c_p - c_v = -T \frac{\left[\left(\partial P/\partial T\right)_v\right]^2}{\left(\partial P/\partial v\right)_T} = \frac{T v \beta^2}{\kappa_T}
{{< /formula >}}

где {{< formula >}}\beta = \frac{1}{v}\left(\frac{\partial v}{\partial T}\right)_P{{< /formula >}} — коэффициент изобарного расширения, {{< formula >}}\kappa_T = -\frac{1}{v}\left(\frac{\partial v}{\partial P}\right)_T{{< /formula >}} — изотермная сжимаемость.

Для идеального газа: {{< formula >}}c_p - c_v = R{{< /formula >}} (постоянная газа).

Для несжимаемой жидкости: {{< formula >}}\kappa_T \to 0{{< /formula >}}, {{< formula >}}\beta \to 0{{< /formula >}}, поэтому {{< formula >}}c_p \approx c_v{{< /formula >}}.

### Отношение теплоёмкостей и скорость звука

{{< formula display="true" >}}
k = \frac{c_p}{c_v} = \frac{\kappa_T}{\kappa_s}, \qquad c_{sound} = \sqrt{\left(\frac{\partial P}{\partial \rho}\right)_s} = \sqrt{k/(\rho\kappa_T)}
{{< /formula >}}

Скорость звука в газах при рабочих условиях определяет критическое давление в расширительных клапанах и соплах.

---

## Применение к построению таблиц свойств

### Алгоритм построения таблиц перегретого пара

1. Измерить P–v–T данные (эксперимент или уравнение состояния)
2. Задать опорную точку: s₀(T_ref, P_ref) = значение из третьего закона или по соглашению
3. Вычислить s(T, P) интегрированием:

{{< formula display="true" >}}
s(T, P) = s_0 + \int_{T_{ref}}^{T} \frac{c_p^{ig}(T')}{T'}\,dT' - \int_{P_{ref}}^{P} \left(\frac{\partial v}{\partial T}\right)_P dP'
{{< /formula >}}

4. Вычислить h(T, P) интегрированием:

{{< formula display="true" >}}
h(T, P) = h_0 + \int_{T_{ref}}^{T} c_p^{ig}(T')\,dT' + \int_{P_{ref}}^{P} \left[v - T\left(\frac{\partial v}{\partial T}\right)_P\right]dP'
{{< /formula >}}

Второй интеграл в обоих выражениях — «поправка на реальный газ», вычисляемая из уравнения состояния.

### Уравнение Бенедикта–Уэбба–Рубина (BWR) и его модификации

Для хладагентов широко применяются модифицированные уравнения BWR (используемые в REFPROP для ряда веществ):

{{< formula display="true" >}}
\frac{P}{\rho RT} = 1 + \frac{B}{\rho} + \frac{C}{\rho^2} + \frac{D}{\rho^3} + \frac{E}{\rho^4} + \frac{F + G/\rho^2}{\rho^2} e^{-\gamma\rho^2}
{{< /formula >}}

Коэффициенты B, C, D, E, F, G — функции температуры, подбираемые по экспериментальным данным. Подробности: NIST Monograph 69 (Thermodynamic Properties of Refrigerants and Refrigerant Mixtures).

---

## Уравнение Гиббса–Дюгема и условие фазового равновесия

Уравнение Гиббса–Дюгема (Gibbs–Duhem equation) для однокомпонентной системы:

{{< formula display="true" >}}
S\,dT - V\,dP + n\,d\mu = 0
{{< /formula >}}

где μ — химический потенциал. При постоянной T и P: {{< formula >}}d\mu = 0{{< /formula >}} — химический потенциал не меняется, что является критерием фазового равновесия.

Для двухфазного равновесия:

{{< formula display="true" >}}
\mu_f(T, P) = \mu_g(T, P) \quad \Longleftrightarrow \quad G_f(T, P) = G_g(T, P)
{{< /formula >}}

Это используется при расчёте летучести и активности в смесях хладагентов — необходимо для ПО типа REFPROP при расчёте свойств смесей (R-410A, R-407C, R-454B).

---

## Коэффициент Джоуля–Томсона

Через соотношения Максвелла:

{{< formula display="true" >}}
\mu_{JT} = \left(\frac{\partial T}{\partial P}\right)_h = \frac{1}{c_p}\left[T\left(\frac{\partial v}{\partial T}\right)_P - v\right] = \frac{v}{c_p}(T\beta - 1)
{{< /formula >}}

{{< table title="Коэффициент Джоуля–Томсона для хладагентов при типичных условиях" >}}
| Хладагент | T, °C | P, МПа | μ_JT, К/МПа | Интерпретация |
|---|---|---|---|---|
| R-134a | 40 (жидкость) | 1,0 | < 0 | Охлаждение при дросселировании |
| R-410A | 40 (жидкость) | 1,5 | < 0 | Охлаждение при дросселировании |
| CO₂ | 40 (пар) | 7,5 | ≈ +0,1 | Малый нагрев выше инверсионной температуры |
| Воздух | 20 | 0,1 | +0,2 | Охлаждение при дросселировании |
{{< /table >}}

Для хладагентов в жидкой фазе μ_JT < 0 — это означает охлаждение при дросселировании, что и является рабочим принципом расширительного клапана.

---

## Инверсионная температура

При инверсионной температуре T_inv коэффициент Джоуля–Томсона меняет знак: {{< formula >}}T\beta = 1{{< /formula >}}, т.е. {{< formula >}}T_{inv} = 1/\beta{{< /formula >}}.

Для идеального газа Ван-дер-Ваальса:

{{< formula display="true" >}}
T_{inv} = \frac{2a}{Rb}
{{< /formula >}}

Для CO₂ инверсионная температура ≈ 1500 К — при комнатных температурах дросселирование CO₂ в газовой фазе приводит к охлаждению (в транскритических системах учитывается при расчёте температуры на выходе газового охладителя).

---

## Частые ошибки при работе с соотношениями свойств

1. **Путаница в постоянных переменных**. {{< formula >}}\left(\partial P/\partial T\right)_v \neq \left(\partial P/\partial T\right)_s{{< /formula >}} — разные физические смыслы.
2. **Применение идеального газа к перегретому пару при высоком давлении**. При P > 0,5 МПа погрешность достигает 3–7 % в значениях cp и s.
3. **Игнорирование h_fg при расчёте кривой насыщения**. Уравнение Клаузиуса–Клапейрона справедливо лишь при малых давлениях. При P > 0,2 P_cr нужно уравнение Клапейрона с реальными v_fg.
4. **Смешение молярных и удельных величин**. Газовая постоянная: {{< formula >}}\bar{R} = 8{,}314{{< /formula >}} кДж/(кмоль·К) — универсальная; {{< formula >}}R = \bar{R}/M{{< /formula >}} — удельная.

## Литература

- Çengel Y. A., Boles M. A. Thermodynamics: An Engineering Approach, 9th ed. McGraw-Hill, 2019, Chapter 12
- Moran M. J. et al. Fundamentals of Engineering Thermodynamics, 9th ed. Wiley, 2018, Chapter 11
- ASHRAE Handbook — Fundamentals (2021), Chapter 2
- Span R., Wagner W. A new equation of state for carbon dioxide covering the fluid region from the triple-point temperature to 1100 K at pressures up to 800 MPa. J. Phys. Chem. Ref. Data, 1996, 25(6)
- Lemmon E. W. et al. NIST Standard Reference Database 23 (REFPROP 10). NIST, 2023
