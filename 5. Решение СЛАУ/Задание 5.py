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

def matrix_vector_product(matrix, vector):
    return [sum(matrix[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matrix))]

def is_close(vector1, vector2, delta=1e-10):
    return all(abs(a - b) < delta for a, b in zip(vector1, vector2))

def gauss_elimination(A, B):
    n = len(A)
    for k in range(n - 1):  
        for i in range(k + 1, n):
            if A[i][k] != 0:
                factor = A[i][k] / A[k][k]
                for j in range(k, n):
                    A[i][j] -= factor * A[k][j]
                for j in range(len(B[0])):
                    B[i][j] -= factor * B[k][j]
    x = [[0] * len(B[0]) for _ in range(n)]
    for col in range(len(B[0])):
        x[n - 1][col] = B[n - 1][col] / A[n - 1][n - 1]  
        for i in range(n - 2, -1, -1):  
            sum_ax = sum(A[i][j] * x[j][col] for j in range(i + 1, n))
            x[i][col] = (B[i][col] - sum_ax) / A[i][i]  
    return x

def verify_solution(A, X, B):
    for col in range(len(B[0])):
        Ax = matrix_vector_product(A, [row[col] for row in X])
        if not is_close(Ax, [row[col] for row in B]):
            return False
    return True

A = [[0, 0, 2, 1, 2], 
     [0, 1, 0, 2, -1], 
     [1, 2, 0, -2, 0], 
     [0, 0, 0, -1, 1], 
     [0, 1, -1, 1, -1]]
B = [[1], 
     [1], 
     [-4], 
     [-2], 
     [-1]]

if is_singular(A):
    print("Коэффициентная матрица A является сингулярной. Система может не иметь единственного решения.")
else:
    solution = gauss_elimination(A, B)
    print("Решение:", solution)

    if verify_solution(A, solution, B):
        print("Решение удовлетворяет уравнению AX = B.")
    else:
        print("Решение не удовлетворяет уравнению AX = B.")