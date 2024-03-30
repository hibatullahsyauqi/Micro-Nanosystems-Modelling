import math
def f(x):
    return math.tan(x)
def five_point_diff(f, x, h):
    return (-25*f(x) + 48*f(x + h) - 36*f(x + 2*h) + 16*f(x + 3*h) - 3*f(x + 4*h)) / (12 * h)
x = 1.2
h = 0.1
epsilon = 1e-10
f_prime_h = five_point_diff(f, x, h)
h /= 2
f_prime_h2 = five_point_diff(f, x, h)
error_estimate = abs((f_prime_h2 - f_prime_h) / (2**5 - 1))
while error_estimate > epsilon:
    h /= 2
    f_prime_h = five_point_diff(f, x, h)
    f_prime_h2 = five_point_diff(f, x, h / 2)
    error_estimate = abs((f_prime_h2 - f_prime_h) / (2**5 - 1))
print("Значение первой производной в точке x = 1.2:", f_prime_h)
print("Погрешность:", error_estimate)
