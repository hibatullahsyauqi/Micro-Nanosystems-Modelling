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
        numpy.ndarray or None: Матрица значений переменных, образующих решение системы уравнений, 
                               либо None, если система сингулярна.
    """
    n = len(A)
    num_eqns = B.shape[1]  # Количество столбцов в B
    X = np.zeros((n, num_eqns))  # Инициализируем матрицу решений

    for col in range(num_eqns):
        # Прямая исключительная операция
        for i in range(n):
            pivot_val = A[i][i]
            if np.abs(pivot_val) < 1e-10:
                print("Система уравнений сингулярна и может не иметь единственного решения.")
                return None  # Система сингулярна
            for j in range(i+1, n):
                ratio = A[j][i] / pivot_val
                for k in range(n):
                    A[j][k] -= ratio * A[i][k]
                B[j][col] -= ratio * B[i][col]

        # Обратная подстановка
        for i in range(n-1, -1, -1):
            summation = sum(A[i][j] * X[j][col] for j in range(i+1, n))
            X[i][col] = (B[i][col] - summation) / A[i][i]

    return X

def check_solution(A, B, X):
    """
    Проверяет решение системы линейных уравнений.

    Args:
        A (numpy.ndarray): Матрица коэффициентов уравнений.
        B (numpy.ndarray): Вектор правых частей уравнений.
        X (numpy.ndarray): Матрица значений переменных, образующих решение системы уравнений.

    Returns:
        bool: True, если решение удовлетворяет условию, False в противном случае.
    """
    if X is None:
        return False  # Система сингулярна
    
    # Выполняем умножение матрицы на матрицу
    result = np.dot(A, X)

    # Проверяем, равен ли результат B
    return np.allclose(result, B)

# Задаем матрицу коэффициентов и вектор правых частей
A = np.array([[2, 0, -1, 0], [0, 1, 2, 0], [-1, 2, 0, 1], [0, 0, 1, -2]], dtype=np.float64)
B = np.array([[1, 0], [0, 0], [0, 1], [0, 0]], dtype=np.float64)

# Вычисляем определитель матрицы A
# det_A = np.linalg.det(A)
# print("Определитель A:", det_A)

# Вызываем функцию для решения уравнений для каждого столбца B
solutions = solve_linear_equations(A, B)
if solutions is not None:
    print("Решение для каждого столбца B:")
    print(solutions)

    # Проверяем, удовлетворяет ли решение условию AX = B для каждого столбца B
    for i, col_solution in enumerate(solutions.T):
        if check_solution(A, B[:, i], col_solution):
            print(f"Решение для столбца {i+1} удовлетворяет условию AX = B.")
        else:
            print(f"Решение для столбца {i+1} не удовлетворяет условию AX = B.")


