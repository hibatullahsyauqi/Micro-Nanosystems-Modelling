import math
import numpy as np

# Рекуррентная формула для вычисления значения интеграла (1)
def compute_integral_recursively(n):
    if n == 0:
        return 1 - 1/math.e
    else:
        return 1 - n * compute_integral_recursively(n - 1)

# Функция для вычисления подынтегральной функции
def f(x, n):
    return x**n * np.exp(x)

# Адаптивная 3-узловая составная квадратура Гаусса
def adaptive_gauss_quad(f, a, b, epsilon, n):
    # 3-узловая квадратура Гаусса
    x = np.array([-np.sqrt(3 / 5), 0, np.sqrt(3 / 5)])
    w = np.array([5 / 9, 8 / 9, 5 / 9])

    stack = [(a, b, 0, 0)]  # Стек для хранения интервалов и значений интегралов
    integral = 0  # Общее значение интеграла
    while stack:
        a, b, integral_ab, error = stack.pop()
        c = (a + b) / 2  # Середина интервала

        # Интегрирование на [a, c] и [c, b]
        integral_ac = np.sum(w * f(((c - a) / 2 * x + (a + c) / 2), n) * (c - a) / 2)
        integral_cb = np.sum(w * f(((b - c) / 2 * x + (b + c) / 2), n) * (b - c) / 2)
        integral_abc = integral_ac + integral_cb

        # Вычисление ошибки
        error = np.abs(integral_abc - integral_ab)

        # Проверка критерия остановки
        if error <= 15 * epsilon or (b - a) < 1e-10:
            integral += integral_abc
        else:
            # Если ошибка больше заданной точности, разделим интервал и добавим оба подинтервала в стек
            stack.append((a, c, integral_ac, error))
            stack.append((c, b, integral_cb, error))

    return integral

# Максимальная допустимая погрешность
max_epsilon = 1e-8

# Вычисление значений интеграла с помощью рекуррентной формулы и адаптивной квадратуры Гаусса
for n in range(31):
    # Вычисление значения интеграла с помощью рекуррентной формулы
    integral_recursive = compute_integral_recursively(n)
    
    # Вычисление значения интеграла с помощью адаптивной квадратуры Гаусса
    integral_gauss = adaptive_gauss_quad(f, 0, 1, max_epsilon, n)
    
    # Вычисление значения ошибки
    error = abs(integral_recursive - integral_gauss)
    
    # Вывод результатов
    print(f"n = {n}, Значение интеграла (рекурсивно): {integral_recursive:.10f}, Значение интеграла (квадратура Гаусса): {integral_gauss:.10f}, Ошибка: {error:.10f}")
    
    # Проверка условия остановки
    if error <= integral_recursive:
        print("Ошибка вычислений становится сравнимой с самим значением интеграла при n =", n)
        break
