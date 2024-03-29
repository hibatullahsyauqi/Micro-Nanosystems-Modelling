import numpy as np
import math

# Функция для вычисления интеграла рекурсивно
def compute_integral_recursively(n):
    # Базовый случай: n = 0
    if n == 0:
        return 1 - 1 / math.e  # Значение интеграла для n = 0
    # Рекурсивный случай: n > 0
    return 1 - n * compute_integral_recursively(n - 1)  # Рекурсивно вычисляем значение интеграла

# Функция, которая определяет подынтегральную функцию
def f(x, n):
    return x ** n * np.exp(x) / math.e  # Подынтегральная функция

# Функция для адаптивной квадратуры Гаусса
def adaptive_gauss_quad(f, a, b, epsilon, n):
    # Узлы и веса квадратурной формулы Гаусса
    x = np.array([-np.sqrt(3 / 5), 0, np.sqrt(3 / 5)])
    w = np.array([5 / 9, 8 / 9, 5 / 9])

    stack = [(a, b, 0)]  # Инициализируем стек с начальными значениями a, b, и интегралом
    integral = 0  # Инициализируем значение интеграла
    error = 0  # Инициализируем значение ошибки
    while stack:
        a, b, integral_ab = stack.pop()  # Извлекаем значения a, b и интеграла из стека
        c = (a + b) / 2  # Находим середину интервала

        # Вычисляем значения подынтегральной функции в точках сетки x
        integral_ac = np.sum(w * f(((c - a) / 2) * x + (a + c) / 2, n) * (c - a) / 2)
        integral_cb = np.sum(w * f(((b - c) / 2) * x + (b + c) / 2, n) * (b - c) / 2)
        integral_abc = integral_ac + integral_cb  # Суммируем значения в точках сетки

        # Проверяем условие останова
        if np.abs(integral_abc - integral_ab) <= epsilon or (b - a) < 1e-10:
            integral += integral_abc  # Добавляем к интегралу значение для текущего интервала
            error += np.abs(integral_abc - integral_ab)  # Обновляем значение ошибки
        else:
            stack.append((a, c, integral_ac))  # Добавляем левую половину интервала в стек
            stack.append((c, b, integral_cb))  # Добавляем правую половину интервала в стек

    return integral, error  # Возвращаем значение интеграла и ошибки

# Поиск значения n
max_epsilon = 1e-10  # Максимальная допустимая ошибка
for n in range(30):
    integral_recursive = compute_integral_recursively(n)  # Вычисляем значение интеграла рекурсивно
    integral_gauss, error = adaptive_gauss_quad(f, 0, 1, max_epsilon, n)  # Вычисляем значение интеграла методом Гаусса
    error_recursive = abs(integral_recursive - integral_gauss)  # Вычисляем ошибку

    # Выводим значения интегралов и ошибки для текущего n
    print(f"n = {n}, Значение интеграла (рекурсивно): {integral_recursive:.10f}, Значение интеграла (квадратура Гаусса): {integral_gauss:.10f}, Ошибка: {error_recursive:.10f}")

    # Проверяем, становится ли ошибка сравнимой с самим значением интеграла
    if error_recursive >= integral_recursive:
        print("Ошибка вычислений становится сравнимой с самим значением интеграла при n =", n)
        break  # Прерываем цикл, если условие выполняется
