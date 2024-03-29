import numpy as np

def check_linear_dependence(A, B):
    """
    Проверяет систему линейных уравнений на линейную зависимость.

    Args:
        A (numpy.ndarray): Матрица коэффициентов уравнений.
        B (numpy.ndarray): Вектор правых частей уравнений.

    Returns:
        bool: True, если система несингулярна (имеет единственное решение), False в противном случае.
    """
    n = len(A)
    for i in range(n):
        # Находим опорную строку с максимальным по модулю элементом в столбце
        pivot_row = np.argmax(np.abs(A[i:, i])) + i
        pivot_value = A[i][i]
        
        if np.abs(pivot_value) < 1e-10:
            return False  # Система сингулярна
        
        # Переставляем строки при необходимости
        if pivot_row != i:
            A[pivot_row], A[i] = A[i].copy(), A[pivot_row].copy()  # Используем копию, чтобы избежать проблем с ссылками
            B[pivot_row], B[i] = B[i].copy(), B[pivot_row].copy()
        
        # Исключаем опорный столбец
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            A[j] -= factor * A[i]
            B[j] -= factor * B[i]
    
    # Проверяем, есть ли нулевой элемент на диагонали
    if any(abs(A[i][i]) < 1e-10 for i in range(n)):
        return False  # Система сингулярна
    
    return True  # Система имеет единственное решение

def solve_linear_equations(A, B):
    """
    Решает систему линейных уравнений методом Гаусса.

    Args:
        A (numpy.ndarray): Матрица коэффициентов уравнений.
        B (numpy.ndarray): Вектор правых частей уравнений.

    Returns:
        list: Список значений переменных, образующих решение системы уравнений.
    """
    n = len(A)

    # Прямая
    for i in range(n):
        pivot_val = A[i][i]
        for j in range(i+1, n):
            ratio = A[j][i] / pivot_val
            for k in range(n):
                A[j][k] -= ratio * A[i][k]
            B[j] -= ratio * B[i]

    # Обратная
    X = [0] * n
    for i in range(n-1, -1, -1):
        summation = sum(A[i][j] * X[j] for j in range(i+1, n))
        X[i] = (B[i] - summation) / A[i][i]

    return X

def check_solution(A, B, X):
    """
    Проверяет решение системы линейных уравнений.

    Args:
        A (numpy.ndarray): Матрица коэффициентов уравнений.
        B (numpy.ndarray): Вектор правых частей уравнений.
        X (list): Решение системы уравнений.

    Returns:
        bool: True, если решение удовлетворяет условию, False в противном случае.
    """
    # Выполняем умножение матрицы на вектор
    result = np.dot(A, X)

    # Проверяем, равен ли результат B
    return np.allclose(result, B)

# Задаем матрицу коэффициентов и вектор правых частей
A = np.array([[2, -3, -1], [3, 2, -5], [2, 4, 1]], dtype=np.float64)
B = np.array([[3], [-9], [-5]], dtype=np.float64)

# Вычисляем определитель матрицы A
# det_A = np.linalg.det(A)
# print("Определитель A:", det_A)

# Проверяем, имеет ли система единственное решение
if check_linear_dependence(A, B):
    # Решаем для X
    X = solve_linear_equations(A, B)
    print("Решение для X:")
    print(X)
else:
    print("Система уравнений сингулярна и может не иметь единственного решения.")
    
# Проверяем, удовлетворяет ли решение условию AX = B
if check_solution(A, B, X):
    print("X удовлетворяет условию AX = B.")
else:
    print("X не удовлетворяет условию AX = B.")
