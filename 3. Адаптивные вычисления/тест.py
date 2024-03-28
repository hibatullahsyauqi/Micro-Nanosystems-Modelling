import numpy as np
from scipy.integrate import quad

# Пример использования
def test_func(x):
    return np.sin(x)

# Вычисление интеграла
integral, error = quad(test_func, 0, 1)
print("Вычисленный интеграл:", integral)