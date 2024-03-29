import math

# Определим функцию
def f(x):
    return math.exp(x)

# Точное значение производной
exact_derivative = math.exp(1)  # Производная от exp(x) равна exp(x), так что значение в точке x=1 равно exp(1)

# Максимальная допустимая погрешность
max_epsilon = 1e-8

'''
Вычисление коэффициентов A и B
Мы хотим избавиться от h^2 слагаемых в разложении по Тейлору,
поэтому у нас получается система уравнений, решив которую, мы найдем коэффициенты A и B
Система уравнений берется из условия равенства коэффициентов при h^2 равным нулю
'''

A = 1/3
B = 2/3

# Вывод коэффициентов
print("Коэффициент A:", A)
print("Коэффициент B:", B)

# Вычисление приближенной производной с использованием новой формулы
def numerical_derivative_combined(x, h):
    derivative = A * (f(x + h/2) - f(x - h/2)) / h + B * (f(x + h) - f(x - h)) / (2*h)
    return derivative

# Вывод заголовка таблицы
print("h\t\t\tdf\t\t\tepsilon (комбинированный метод)")

# Начальное значение h
h = 0.1

# Пока погрешность больше максимальной допустимой
while h >= max_epsilon:
    # Вычисление численной производной с использованием комбинированного метода
    numerical_result_combined = numerical_derivative_combined(1, h)
    # Оценка погрешности
    error_combined = abs(exact_derivative - numerical_result_combined)
    # Вывод результатов
    print(f"{h:.10f}\t\t{numerical_result_combined:.10f}\t\t{error_combined:.10f}")
    # Уменьшение h в 10 раз
    h /= 10
