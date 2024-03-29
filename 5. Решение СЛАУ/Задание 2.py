def gauss_elimination(A, B):
    # Проверка совместности системы
    if len(A) != len(B):
        return "Несовместная система"

    # Прямой ход метода Гаусса
    n = len(A)
    for i in range(n):
        # Поиск максимального элемента в столбце
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k

        # Обмен строк
        A[i], A[max_row] = A[max_row], A[i]
        B[i], B[max_row] = B[max_row], B[i]

        # Приведение к диагональному виду
        for k in range(i + 1, n):
            factor = A[k][i] / A[i][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            B[k] -= factor * B[i]

    # Обратный ход метода Гаусса
    X = [0] * n
    for i in range(n - 1, -1, -1):
        X[i] = B[i]
        for j in range(i + 1, n):
            X[i] -= A[i][j] * X[j]
        X[i] /= A[i][i]

    return X

# Матрица A и вектор B из вашего примера
A = [[2, -3, -1],
     [3, 2, -5],
     [2, 4, 1]]

B = [3, -9, -5]

# Решение системы уравнений
solution = gauss_elimination(A, B)
print("Solution:")
print("x =", solution[0])
print("y =", solution[1])
print("z =", solution[2])