import numpy as np
from LUdecomp import LUdecomp, LUsolve

# Определение матрицы A и вектора B
A = np.array([[2, -3, -1],
              [3, 2, -5],
              [2, 4, 1]])
B = np.array([3, -9, -5])

# LU-разложение матрицы A
LU = LUdecomp(A.copy())

# Решение системы уравнений
solution = LUsolve(LU, B.copy())

# Вывод решения
print("Решение:", solution)
