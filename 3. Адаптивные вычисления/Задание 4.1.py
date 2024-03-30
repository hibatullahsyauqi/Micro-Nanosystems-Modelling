import numpy as np

def f(x):
    return np.sin(x)

def gauss_quad_3_nodes(a, b, n):
    x = np.array([-np.sqrt(3 / 5), 0, np.sqrt(3 / 5)])
    w = np.array([5 / 9, 8 / 9, 5 / 9])

    h = (b - a) / n  # Step
    integral = 0
    for i in range(n):
        xi = a + i * h
        for j in range(3):
            integral += w[j] * f(xi + (h / 2) * (x[j] + 1))
    integral *= h / 2
    return integral

def adaptive_gauss_quad(a, b, epsilon):
    I_h = gauss_quad_3_nodes(a, b, 2)
    I_h2 = gauss_quad_3_nodes(a, b, 4)
    error_estimate = abs((1 / (2**3 - 1)) * (I_h - I_h2))
    if error_estimate < epsilon:
        return I_h, error_estimate
    else:
        mid = (a + b) / 2
        return adaptive_gauss_quad(a, mid, epsilon / 2) + adaptive_gauss_quad(mid, b, epsilon / 2)

# Integration interval
a = 0
b = 1

# Specified absolute error
epsilon = 1e-8

# Compute the integral with the specified absolute error
integral, error_estimate = adaptive_gauss_quad(a, b, epsilon)
print("Integral value:", integral)
print("Error estimate:", error_estimate)
