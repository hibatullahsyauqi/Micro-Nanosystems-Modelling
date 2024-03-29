import numpy as np

# Определение функции метода Гаусса
def gaussian_elimination(A, B):
    n = len(A)

    # Прямой ход метода Гаусса
    for i in range(n):
        # Поиск максимального элемента в столбце для частичного выбора
        max_row = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_row][i]):
                max_row = j

        # Обмен строк
        A[i], A[max_row] = A[max_row], A[i]
        B[i], B[max_row] = B[max_row], B[i]

        # Приведение к диагональному виду
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            B[j] -= factor * B[i]

    # Обратный ход метода Гаусса
    X = [0] * n
    for i in range(n - 1, -1, -1):
        X[i] = B[i] / A[i][i]
        for j in range(i):
            B[j] -= A[j][i] * X[i]

    return X

# Матрица A и матрица B
A = np.array([[6, -4, 1],
              [-4, 6, -4],
              [1, -4, 6]])

B = np.array([[-14, 22],
              [36, -18],
              [6, 7]])

# Решение системы уравнений с помощью метода Гаусса
solution_1 = gaussian_elimination(A, [b[0] for b in B])
solution_2 = gaussian_elimination(A, [b[1] for b in B])

# Вывод результатов для Solution 1
print("Solution 1:")
print("Gaussian Elimination:")
print("x1 =", solution_1[0])
print("x2 =", solution_1[1])
print("x3 =", solution_1[2])

# Вывод результатов для Solution 2
print("Solution 2:")
print("Gaussian Elimination:")
print("x1 =", solution_2[0])
print("x2 =", solution_2[1])
print("x3 =", solution_2[2])

# Проверка решений
# Проверка для Solution 1
print("Check Solution 1:")
print("A * solution_1 =", np.dot(A, solution_1))
print("B[:, 0] =", B[:, 0])

# Проверка для Solution 2
print("\nCheck Solution 2:")
print("A * solution_2 =", np.dot(A, solution_2))
print("B[:, 1] =", B[:, 1])