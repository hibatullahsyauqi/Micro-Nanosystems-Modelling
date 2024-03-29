import numpy as np

def adaptive_gauss_quad(f, a, b, epsilon):
    # 3-узловая квадратура Гаусса
    x = np.array([-np.sqrt(3 / 5), 0, np.sqrt(3 / 5)])
    w = np.array([5 / 9, 8 / 9, 5 / 9])

    stack = [(a, b, 0)]  # Стек для хранения интервалов и значений интегралов
    integral = 0  # Общее значение интеграла
    error = 0  # Общее значение погрешности
    while stack:
        a, b, integral_ab = stack.pop()
        c = (a + b) / 2  # Середина интервала

        # Интегрирование на [a, c] и [c, b]
        integral_ac = np.sum(w * f((c - a) / 2 * x + (a + c) / 2)) * (c - a) / 2
        integral_cb = np.sum(w * f((b - c) / 2 * x + (b + c) / 2)) * (b - c) / 2
        integral_abc = integral_ac + integral_cb

        # Проверка критерия остановки по абсолютной погрешности
        if np.abs(integral_abc - integral_ab) <= epsilon or (b - a) < 1e-10:
            integral += integral_abc
            error += np.abs(integral_abc - integral_ab)
        else:
            # Если погрешность больше заданной точности, разделим интервал и добавим оба подинтервала в стек
            stack.append((a, c, integral_ac))
            stack.append((c, b, integral_cb))

    return integral, error

# Пример использования
def f(x):
    return np.cosh(x)

integral, error = adaptive_gauss_quad(f, 0, 1, 1e-8)
print("Приближенное значение интеграла:", integral)
print("Погрешность:", error)
