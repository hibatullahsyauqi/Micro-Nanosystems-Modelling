import math
def f(x):
    if x == 0:
        return 0
    else:
        return math.sin(x) / math.sqrt(x)
def simpsons_rule(a, b, n):
    h = (b - a) / n
    sum_odd = 0
    sum_even = 0
    for i in range(1, n, 2):
        x = a + i * h
        sum_odd += f(x)
    for i in range(2, n, 2):
        x = a + i * h
        sum_even += f(x)
    integral = f(a) + f(b) + 4 * sum_odd + 2 * sum_even
    integral *= h / 3
    return integral
a = 0
b = 1
N = 2
epsilon = 1e-10
I_h = simpsons_rule(a, b, N)
I_h2 = simpsons_rule(a, b, 2 * N)
error_estimate = abs((I_h2 - I_h) / (2**5 - 1))
while error_estimate > epsilon:
    N *= 2
    I_h = simpsons_rule(a, b, N)
    I_h2 = simpsons_rule(a, b, 2 * N)
    error_estimate = abs((I_h2 - I_h) / (2**5 - 1))
print("Значение интеграла:", I_h)
print("Погрешность:", error_estimate)