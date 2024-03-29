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
print("h\t\t\tПриближенная производная\t\t\tПогрешность")

# Пока погрешность больше максимальной допустимой
while h >= max_epsilon:
    # Вычисляем численную производную
    numerical_result = (f(1 + h) - f(1)) / h
    # Оцениваем погрешность
    error = abs(exact_derivative - numerical_result)
    # Выводим результаты
    print(f"{h:.10f}\t\t{numerical_result:.10f}\t\t\t{error:.10f}")
    # Уменьшаем h в 10 раз
    h /= 10
