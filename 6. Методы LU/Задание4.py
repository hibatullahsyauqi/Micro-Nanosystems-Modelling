import numpy as np
from LUdecomp import LUdecomp, LUsolve

# Определение матрицы A и матрицы B
A = np.array([[2, 0, -1, 0], 
              [0, 1, 2, 0], 
              [-1, 2, 0, 1], 
              [0, 0, 1, -2]])
B = np.array([[1, 0], 
              [0, 0], 
              [0, 1], 
              [0, 0]])

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
