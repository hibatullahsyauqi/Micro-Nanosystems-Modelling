import math

# Определим функцию
def f(x):
    return math.exp(x)

# Точное значение производной
exact_derivative = math.exp(1)  # Производная от exp(x) равна exp(x), так что значение в точке x=1 равно exp(1)

# Максимальная допустимая абсолютная погрешность
max_epsilon = 1e-8

# Вычисление коэффициентов A и B
A = 1/3
B = 2/3

# Вывод коэффициентов
print("Коэффициент A:", A)
print("Коэффициент B:", B)

# Вычисление приближенной производной с использованием новой формулы
def numerical_derivative_combined(x, h):
    derivative = A * (f(x + h/2) - f(x - h/2)) / h + B * (f(x + h) - f(x - h)) / (2*h)
    return derivative

# Функция для адаптивного вычисления производной
def adaptive_numerical_derivative(f, x, epsilon):
    h = 0.1  # Начальное значение шага
    while True:
        # Вычисляем производную с текущим шагом
        derivative = numerical_derivative_combined(x, h)
        # Оцениваем погрешность
        error = abs(exact_derivative - derivative)
        # Если погрешность укладывается в заданную абсолютную погрешность, возвращаем результат
        if error <= epsilon:
            return derivative, h, error
        # В противном случае уменьшаем шаг вдвое
        h /= 2

# Вызываем функцию для вычисления производной с адаптивным выбором шага
approx_derivative, step_size, error = adaptive_numerical_derivative(f, 1, max_epsilon)
print("Приближенное значение производной:", approx_derivative)
print("Размер шага:", step_size)
print("Погрешность:", error)
