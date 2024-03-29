def is_linearly_dependent(matrix):
    """
    Проверяет, линейно зависимы ли строки матрицы.
    """
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            if matrix[j][i] != 0:
                return True  # Система является сингулярной
    return False  # Система имеет единственное решение

def gaussian_elimination(A, B):
    """
    Выполняет метод Гаусса для решения системы уравнений AX = B.
    """
    n = len(A)
    
    # Прямой ход
    for i in range(n):
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            B[j][0] -= factor * B[i][0]
    
    # Обратный ход
    X = [0] * n
    for i in range(n - 1, -1, -1):
        X[i] = B[i][0] / A[i][i]
        for j in range(i + 1, n):
            X[i] -= A[i][j] * X[j] / A[i][i]
    
    return X

def verify_solution(A, X, B):
    """
    Проверяет, удовлетворяет ли решение X уравнению AX = B.
    """
    return all(abs(sum(A[i][j] * X[j] for j in range(len(X))) - B[i][0]) < 1e-10 for i in range(len(B)))

# Пример использования
A = [[2, -3, -1],
     [3, 2, -5],
     [2, 4, 1]]

B = [[3],
     [-9],
     [-5]]

if is_linearly_dependent(A):
    print("Система является сингулярной. Нет единственного решения.")
else:
    X = gaussian_elimination(A, B)
    print("Решение X:", X)
    if verify_solution(A, X, B):
        print("Решение удовлетворяет уравнению AX = B.")
    else:
        print("Решение не удовлетворяет уравнению AX = B.")
