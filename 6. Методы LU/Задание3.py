import numpy as np
from LUdecomp import LUdecomp, LUsolve

# Определение матрицы A и вектора B
A = np.array([[6, -4, 1],
              [-4, 6, -4],
              [1, -4, 6]])
B = np.array([[-14, 22],
              [36, -18],
              [6, 7]])

# LU-разложение матрицы A
LU = LUdecomp(A.copy())

# Решение системы уравнений
solution = []
for b in B.T:  # Транспонирование B для итерации по столбцам
    x = LUsolve(LU, b.copy())
    solution.append(x)

solution = np.array(solution)

# Вывод решения
print("Решение:")
print(solution)
