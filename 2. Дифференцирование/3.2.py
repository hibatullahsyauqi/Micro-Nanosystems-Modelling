import math

# Определим функцию
def f(x):
    return math.exp(x)

# Точное значение производной
exact_derivative = math.exp(1)  # Производная от exp(x) равна exp(x), так что значение в точке x=1 равно exp(1)

# Максимальная допустимая погрешность
max_epsilon = 1e-8

# Начальное значение h
h = 0.1

# Вывод заголовка таблицы
print("h\t\tdf (конечная разность)\tdf (симметризованная разность)\tepsilon (конечная разность)\tepsilon (симметризованная разность)")

# Пока погрешность больше максимальной допустимой
while h >= max_epsilon:
    # Конечная разность
    numerical_result_fd = (f(1 + h) - f(1)) / h
    # Симметризованная разность
    numerical_result_sd = (f(1 + h/2) - f(1 - h/2)) / h
    # Оцениваем погрешность (конечная разность)
    error_fd = abs(exact_derivative - numerical_result_fd)
    # Оцениваем погрешность (симметризованная разность)
    error_sd = abs(exact_derivative - numerical_result_sd)
    # Выводим результаты
    print(f"{h:.10f}\t{numerical_result_fd:.10f}\t\t{numerical_result_sd:.10f}\t\t\t{error_fd:.10f}\t\t\t{error_sd:.10f}")
    # Уменьшаем h в 10 раз
    h /= 10
