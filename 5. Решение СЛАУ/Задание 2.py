def determinant(matrix):
    n = len(matrix)
    if n == 1:  # Если матрица размером 1x1
        return matrix[0][0]  # Возвращаем элемент матрицы
    elif n == 2:  # Если матрица размером 2x2
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]  # Возвращаем определитель по формуле для 2x2 матрицы
    else:  # Если матрица размером больше 2x2
        det = 0
        for j in range(n):
            det += ((-1) ** j) * matrix[0][j] * determinant(minor(matrix, 0, j))
            # Рекурсивно вычисляем определитель, используя миноры
        return det

def minor(matrix, row, col):
    return [row[:col] + row[col+1:] for row in (matrix[:row] + matrix[row+1:])]
    # Функция для получения минора матрицы

def is_singular(matrix):
    return determinant(matrix) == 0
    # Функция для проверки, является ли матрица сингулярной (определитель равен нулю)

def matrix_vector_product(matrix, vector):
    return [sum(matrix[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matrix))]
    # Функция для умножения матрицы на вектор

def is_close(vector1, vector2, delta=1e-10):
    return all(abs(a - b) < delta for a, b in zip(vector1, vector2))
    # Функция для сравнения векторов на близость

def gauss_elimination(A, B):
    n = len(A)
    for k in range(n - 1):  # Прямой ход метода Гаусса
        for i in range(k + 1, n):
            if A[i][k] != 0:
                factor = A[i][k] / A[k][k]
                for j in range(k, n):
                    A[i][j] -= factor * A[k][j]
                B[i] -= factor * B[k]
    x = [0] * n
    x[n - 1] = B[n - 1] / A[n - 1][n - 1]  # Решение для последнего уравнения
    for i in range(n - 2, -1, -1):  # Обратный ход метода Гаусса
        sum_ax = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (B[i] - sum_ax) / A[i][i]  # Вычисление решения для остальных уравнений
    return x

def verify_solution(A, x, B):
    Ax = matrix_vector_product(A, x)  # Умножаем матрицу на вектор решения
    return is_close(Ax, B)  # Проверяем, соответствует ли полученный вектор правой части системы

A = [[2, -3, -1],
    [3, 2, -5],
    [2, 4, 1]]
B = [3, -9, -5]

if is_singular(A):
    print("Коэффициентная матрица A является сингулярной. Система может не иметь единственного решения.")
else:
    solution = gauss_elimination(A, B)  # Решаем систему методом Гаусса
    print("Решение:", solution)

    if verify_solution(A, solution, B):
        print("Решение удовлетворяет уравнению AX = B.")
    else:
        print("Решение не удовлетворяет уравнению AX = B.")