import math

# Определение функции
def f(x):
    return math.exp(x)

# Точное значение второй производной
exact_second_derivative = math.exp(1)  # Вторая производная от exp(x) также равна exp(x), поэтому значение в точке x=1 равно exp(1)

# Минимальная и максимальная допустимая погрешность
max_epsilon = 1e-8
min_epsilon = 1e-2

# Вычисление коэффициентов A, B, C
A = -1 / 12  # Коэффициент при f(x+2h)
B = 4 / 3  # Коэффициент при f(x+h) и f(x-h)
C = -5 / 2   # Коэффициент при f(x)

# Вывод коэффициентов
print("Коэффициент A:", A)
print("Коэффициент B:", B)
print("Коэффициент C:", C)

# Функция для вычисления второй производной с использованием формулы (2.3.12)
def numerical_second_derivative(x, h):
    derivative = (A * f(x + 2 * h) + B * f(x + h) + C * f(x) + B * f(x - h) + A * f(x - 2 * h)) / (h ** 2)
    return derivative

# Вывод заголовка таблицы
print("h\t\t\tddf\t\tepsilon\t\tОтношение ошибки к h^2")

# Начальное значение h
h = 0.1

# Пока погрешность больше максимальной допустимой
while h >= max_epsilon:
    # Вычисление численной второй производной
    numerical_result = numerical_second_derivative(1, h)
    # Оценка погрешности
    error = abs(exact_second_derivative - numerical_result)
    # Оценка порядка аппроксимации
    if h > min_epsilon:
        order_of_accuracy = "---"  # Не учитываем первые несколько итераций для оценки порядка аппроксимации
    else:
        order_of_accuracy = error / (h ** 2)
        order_of_accuracy = "{:.10f}".format(order_of_accuracy)  # Преобразуем в строку с заданным форматом
    # Вывод результатов
    print("{:.10f}\t\t{:.10f}\t\t{:.10f}\t\t{}".format(h, numerical_result, error, order_of_accuracy))
    # Уменьшение h в 10 раз
    h /= 10
