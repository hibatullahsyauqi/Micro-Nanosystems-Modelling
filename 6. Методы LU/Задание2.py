import numpy as np
from LUdecomp import LUdecomp, LUsolve

def determinant(matrix):
    """
    Calculate the determinant of a square matrix using LU decomposition.

    Parameters:
        matrix: list of lists
            The square matrix.

    Returns:
        det: float
            The determinant of the matrix.
    """
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    else:
        lu = LUdecomp(np.array(matrix))
        det = np.prod(np.diagonal(lu))
        return det

def is_singular(matrix):
    """
    Check if a matrix is singular (determinant equals zero).

    Parameters:
        matrix: list of lists
            The matrix.

    Returns:
        bool: True if the matrix is singular, False otherwise.
    """
    return determinant(matrix) == 0

def matrix_vector_product(matrix, vector):
    """
    Perform matrix-vector multiplication.

    Parameters:
        matrix: list of lists
            The matrix.
        vector: list
            The vector.

    Returns:
        result: list
            The result of the multiplication.
    """
    return np.dot(matrix, vector)

def verify_solution(A, x, B):
    """
    Verify if the solution satisfies the equation AX = B.

    Parameters:
        A: list of lists
            Coefficient matrix.
        x: list
            Solution vector.
        B: list
            Right-hand side vector.

    Returns:
        bool: True if the solution satisfies the equation, False otherwise.
    """
    Ax = matrix_vector_product(A, x)
    return np.allclose(Ax, B)

A = [[2, -3, -1],
    [3, 2, -5],
    [2, 4, 1]]
B = [3, -9, -5]

if is_singular(A):
    print("Коэффициентная матрица A является сингулярной. Система может не иметь единственного решения.")
else:
    lu = LUdecomp(np.array(A))
    solution = LUsolve(lu, np.array(B))
    print("Решение:", solution)

    if verify_solution(A, solution, B):
        print("Решение удовлетворяет уравнению AX = B.")
    else:
        print("Решение не удовлетворяет уравнению AX = B.")
