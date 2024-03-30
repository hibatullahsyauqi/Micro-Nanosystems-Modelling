def f(x):
    return x**5 + 3*x**3 - 2

# Интервал интегрирования
a = 0
b = 2

# Начальное количество интервалов
N = 10

# Мин погрешность
target_error = 1e-10

# Вычисление интеграла
def simpson_rule(a, b, N):
    h = (b - a) / N
    sum_odd = sum_even = 0
    for i in range(1, N, 2):
        sum_odd += f(a + i * h)
    for i in range(2, N-1, 2):
        sum_even += f(a + i * h)
    integral = (f(a) + 4 * sum_odd + 2 * sum_even + f(b)) * h / 3
    return integral

# Оценка погрешности
def runge_error(I_h, I_h2, n):
    return abs((1 / (2**n - 1)) * (I_h - I_h2))

I_h = simpson_rule(a, b, N)
I_h2 = simpson_rule(a, b, 2 * N)
error_estimate = runge_error(I_h, I_h2, 5)

while error_estimate > target_error:
    N *= 2
    I_h = simpson_rule(a, b, N)
    I_h2 = simpson_rule(a, b, 2 * N)
    error_estimate = runge_error(I_h, I_h2, 5)

print("Значение интеграла:", I_h)
print("Погрешность:", error_estimate)
