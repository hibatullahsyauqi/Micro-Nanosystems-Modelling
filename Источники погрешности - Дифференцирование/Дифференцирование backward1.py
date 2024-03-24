import math

def f(x):
    return math.exp(x)

def approximation(x, h):
    return f(x + h/2) - f(x - h/2)

def derivative(x, h):
    return (approximation(x + h, h) - approximation(x - h, h)) / (2*h)

def find_max_order():
    A = B = 0
    max_error = 0
    for i in range(1, 10):
        for j in range(1, 10):
            h = 0.1
            while h >= 0.0001:  # Adjust the stopping condition as needed
                error = abs(derivative(1, h) - (i*(approximation(1 + h/2, h) - approximation(1 - h/2, h))/h) + j*(approximation(1 + h, h) - approximation(1 - h, h))/(2*h))
                if error > max_error:
                    max_error = error
                    A = i
                    B = j
                h /= 2  # Recurse h by halving its value
    return A, B, max_error

A, B, max_error = find_max_order()
print(f"Max approximation order: A = {A}, B = {B}")
print(f"Max error: {max_error}")