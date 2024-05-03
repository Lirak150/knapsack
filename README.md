# Алгоритмы исследования операций, лабораторная работа 2

## ТЗ:

Реализовать и сравнить алгоритмы для решения knapsack 0-1 problem.

1) 2-approx алгоритм.
2) ДП на весах или ДП на стоимостях (был выбран ДП на весах).
3) Метод ветвей и границ используя задачу LP или используя только 1 предмет (был выбран алгоритм используя 1 предмет).
4) PTAS или FPTAS (был выбран PTAS).

Необходимо сравнить время работы алгоритма, количество промежуточных решений и итоговый profit рюкзака.

## Структура файлов

- tests - тесты (в директориях тесты, в tests.py парсинг этих тестов)
- two_approx.py - реализация 2-approximation
- dp_on_weights.py - реализация ДП на весах
- ptas.py - реализация PTAS
- branch_and_bound.py - реализация алгоритма, используя 1 предмет на каждой итерации.
- main.py - запускает тестов и выводит метрики для каждого алгоритма.

## Итоги

* Test p01:
  * Capacity: 165
  * Optimal profit: 309 
  * Optimal choice: [1, 1, 1, 1, 0, 1, 0, 0, 0, 0]
  * DP on weights profit: 309 
  * DP on weights weight: 165 
  * DP on weights choice: [1, 1, 1, 1, 0, 1, 0, 0, 0, 0]
  * DP number of intermediate solutions: 1826 
  * DP time: 0.00019 
  * 2-approx profit: 309 
  * 2-approx weight: 165 
  * 2-approx choice: [1, 1, 1, 1, 0, 1, 0, 0, 0, 0]
  * 2-approx number of intermediate solutions: 2 
  * 2-approx time: 3.1e-06 
  * PTAS with PTAS_POLYNOMIAL_CONST=4 profit: 309 
  * PTAS with PTAS_POLYNOMIAL_CONST=4 weight: 165 
  * PTAS with PTAS_POLYNOMIAL_CONST=4 choice: [1, 1, 1, 1, 0, 1, 0, 0, 0, 0]
  * PTAS with PTAS_POLYNOMIAL_CONST=4 number of intermediate solutions: 385 
  * PTAS with PTAS_POLYNOMIAL_CONST=4 time: 0.00034 
  * branch_and_cut profit: 309 
  * branch_and_cut weight: 165 
  * branch_and_cut choice: [1, 1, 1, 1, 0, 1, 0, 0, 0, 0]
  * branch_and_cut number of intermediate solutions: 456 
  * branch_and_cut time: 0.00055
* Test p02:
  * Capacity: 26 
  * Optimal profit: 51 
  * Optimal choice: [0, 1, 1, 1, 0]
  * DP on weights profit: 51 
  * DP on weights weight: 26 
  * DP on weights choice: [0, 1, 1, 1, 0]
  * DP number of intermediate solutions: 162 
  * DP time: 1.8e-05 
  * 2-approx profit: 47 
  * 2-approx weight: 23 
  * 2-approx choice: [1, 1, 0, 0, 0]
  * 2-approx number of intermediate solutions: 2 
  * 2-approx time: 1.6e-06 
  * PTAS with PTAS_POLYNOMIAL_CONST=4 profit: 51 
  * PTAS with PTAS_POLYNOMIAL_CONST=4 weight: 26 
  * PTAS with PTAS_POLYNOMIAL_CONST=4 choice: [0, 1, 1, 1, 0]
  * PTAS with PTAS_POLYNOMIAL_CONST=4 number of intermediate solutions: 30 
  * PTAS with PTAS_POLYNOMIAL_CONST=4 time: 2.6e-05 
  * branch_and_cut profit: 51 
  * branch_and_cut weight: 26 
  * branch_and_cut choice: [0, 1, 1, 1, 0]
  * branch_and_cut number of intermediate solutions: 36 
  * branch_and_cut time: 4.5e-05
* Test p03:
  * Capacity: 190
  * Optimal profit: 150
  * Optimal choice: [1, 1, 0, 0, 1, 0]
  * DP on weights profit: 150
  * DP on weights weight: 190
  * DP on weights choice: [1, 1, 0, 0, 1, 0]
  * DP number of intermediate solutions: 1337
  * DP time: 0.00014
  * 2-approx profit: 146
  * 2-approx weight: 179
  * 2-approx choice: [1, 1, 0, 1, 0, 0]
  * 2-approx number of intermediate solutions: 2
  * 2-approx time: 1.6e-06
  * PTAS with PTAS_POLYNOMIAL_CONST=4 profit: 150
  * PTAS with PTAS_POLYNOMIAL_CONST=4 weight: 190
  * PTAS with PTAS_POLYNOMIAL_CONST=4 choice: [1, 1, 0, 0, 1, 0]
  * PTAS with PTAS_POLYNOMIAL_CONST=4 number of intermediate solutions: 56
  * PTAS with PTAS_POLYNOMIAL_CONST=4 time: 5.2e-05
  * branch_and_cut profit: 150
  * branch_and_cut weight: 190
  * branch_and_cut choice: [1, 1, 0, 0, 1, 0]
  * branch_and_cut number of intermediate solutions: 56
  * branch_and_cut time: 5.7e-05
* Test p04:
  * Capacity: 50
  * Optimal profit: 107
  * Optimal choice: [1, 0, 0, 1, 0, 0, 0]
  * DP on weights profit: 107
  * DP on weights weight: 50
  * DP on weights choice: [1, 0, 0, 1, 0, 0, 0]
  * DP number of intermediate solutions: 408
  * DP time: 5.1e-05
  * 2-approx profit: 102
  * 2-approx weight: 48
  * 2-approx choice: [1, 1, 0, 0, 1, 1, 0]
  * 2-approx number of intermediate solutions: 2
  * 2-approx time: 1.6e-06
  * PTAS with PTAS_POLYNOMIAL_CONST=4 profit: 107
  * PTAS with PTAS_POLYNOMIAL_CONST=4 weight: 50
  * PTAS with PTAS_POLYNOMIAL_CONST=4 choice: [1, 0, 0, 1, 0, 0, 0]
  * PTAS with PTAS_POLYNOMIAL_CONST=4 number of intermediate solutions: 98
  * PTAS with PTAS_POLYNOMIAL_CONST=4 time: 0.0001
  * branch_and_cut profit: 107
  * branch_and_cut weight: 50
  * branch_and_cut choice: [1, 0, 0, 1, 0, 0, 0]
  * branch_and_cut number of intermediate solutions: 32
  * branch_and_cut time: 3.9e-05

* Test p05:
  * Capacity: 104
  * Optimal profit: 900
  * Optimal choice: [1, 0, 1, 1, 1, 0, 1, 1]
  * DP on weights profit: 900
  * DP on weights weight: 104
  * DP on weights choice: [1, 0, 1, 1, 1, 0, 1, 1]
  * DP number of intermediate solutions: 945
  * DP time: 0.00011
  * 2-approx profit: 858
  * 2-approx weight: 97
  * 2-approx choice: [1, 1, 0, 1, 1, 1, 1, 1]
  * 2-approx number of intermediate solutions: 2
  * 2-approx time: 1.8e-06
  * PTAS with PTAS_POLYNOMIAL_CONST=4 profit: 900
  * PTAS with PTAS_POLYNOMIAL_CONST=4 weight: 104
  * PTAS with PTAS_POLYNOMIAL_CONST=4 choice: [1, 0, 1, 1, 1, 0, 1, 1]
  * PTAS with PTAS_POLYNOMIAL_CONST=4 number of intermediate solutions: 162
  * PTAS with PTAS_POLYNOMIAL_CONST=4 time: 0.00023
  * branch_and_cut profit: 900
  * branch_and_cut weight: 104
  * branch_and_cut choice: [1, 0, 1, 1, 1, 0, 1, 1]
  * branch_and_cut number of intermediate solutions: 78
  * branch_and_cut time: 9.2e-05
* Test p06:
  * Capacity: 170
  * Optimal profit: 1735
  * Optimal choice: [0, 1, 0, 1, 0, 0, 1]
  * DP on weights profit: 1735
  * DP on weights weight: 169
  * DP on weights choice: [0, 1, 0, 1, 0, 0, 1]
  * DP number of intermediate solutions: 1368
  * DP time: 0.00014
  * 2-approx profit: 1478
  * 2-approx weight: 140
  * 2-approx choice: [1, 1, 1, 0, 0, 0, 0]
  * 2-approx number of intermediate solutions: 2
  * 2-approx time: 1.8e-06
  * PTAS with PTAS_POLYNOMIAL_CONST=4 profit: 1735
  * PTAS with PTAS_POLYNOMIAL_CONST=4 weight: 169
  * PTAS with PTAS_POLYNOMIAL_CONST=4 choice: [0, 1, 0, 1, 0, 0, 1]
  * PTAS with PTAS_POLYNOMIAL_CONST=4 number of intermediate solutions: 98
  * PTAS with PTAS_POLYNOMIAL_CONST=4 time: 9.6e-05
  * branch_and_cut profit: 1735
  * branch_and_cut weight: 169
  * branch_and_cut choice: [0, 1, 0, 1, 0, 0, 1]
  * branch_and_cut number of intermediate solutions: 160
  * branch_and_cut time: 0.0002
* Test p07:
  * Capacity: 750
  * Optimal profit: 1458
  * Optimal choice: [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1]
  * DP on weights profit: 1458
  * DP on weights weight: 749
  * DP on weights choice: [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1]
  * DP number of intermediate solutions: 12016
  * DP time: 0.0016
  * 2-approx profit: 1441
  * 2-approx weight: 740
  * 2-approx choice: [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0]
  * 2-approx number of intermediate solutions: 2
  * 2-approx time: 3.3e-06
  * PTAS with PTAS_POLYNOMIAL_CONST=4 profit: 1448
  * PTAS with PTAS_POLYNOMIAL_CONST=4 weight: 749
  * PTAS with PTAS_POLYNOMIAL_CONST=4 choice: [1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1]
  * PTAS with PTAS_POLYNOMIAL_CONST=4 number of intermediate solutions: 1940
  * PTAS with PTAS_POLYNOMIAL_CONST=4 time: 0.0034
  * branch_and_cut profit: 1458
  * branch_and_cut weight: 749
  * branch_and_cut choice: [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1]
  * branch_and_cut number of intermediate solutions: 5600
  * branch_and_cut time: 0.0076