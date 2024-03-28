import math

def f(x):
    return math.sin(x)

def gauss_legendre_3(f, a, b):
    nodes = [-math.sqrt(3/5), 0, math.sqrt(3/5)]
    weights = [5/9, 8/9, 5/9]
    
    result = 0
    for i in range(3):
        x = 0.5 * ((b - a) * nodes[i] + a + b)
        result += weights[i] * f(x)
    
    return 0.5 * (b - a) * result

def runge_adaptive_integration(f, a, b, eps, threshold=1e-6):
    h = b - a
    I_1 = gauss_legendre_3(f, a, b)
    I_2 = gauss_legendre_3(f, a, a + h/2) + gauss_legendre_3(f, a + h/2, b)
    ratio = 30 * eps / h * abs(I_2 - I_1)
    
    if ratio < threshold:
        return I_2
    else:
        return runge_adaptive_integration(f, a, a + h/2, eps/2) + runge_adaptive_integration(f, a + h/2, b, eps/2)

# Example usage
result = runge_adaptive_integration(f, 0, 1, 1e-8)
print(f"Result: {result}")