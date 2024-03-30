def determinant(matrix):
    n = len(matrix)
    # случай для матрицы 2x2
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    # случай для матрицы nxn
    else:
        det = 0
        for j in range(n):
            det += (-1) ** j * matrix[0][j] * determinant(minor(matrix, 0, j))
        return det

def minor(matrix, row, col):
    return [row[:col] + row[col+1:] for row in (matrix[:row] + matrix[row+1:])]

# Матрица A
A = [[2.11, -0.80, 1.72],
     [-1.84, 3.03, 1.29],
     [-1.57, 5.25, 4.30]]

# Вычисляем определитель матрицы A
det_A = determinant(A)

# Проверяем, является ли определитель нулем
if det_A == 0:
    print("Матрицы линейно-зависимы")
else:
    print("Матрицы линейно-независимы")

