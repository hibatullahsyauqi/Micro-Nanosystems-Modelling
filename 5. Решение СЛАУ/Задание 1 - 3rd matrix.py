# Определение матрицы A
A = [[2, -1, 0],
     [-1, 2, -1],
     [0, -1, 2]]

# Вычисление определителя для 3x3 матрицы
def determinant(matrix):
    return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
            matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
            matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))

# Проверка на линейную зависимость
det_A = determinant(A)
if det_A == 0:
    print("Матрицы линейно зависимы.")
else:
    print("Матрицы линейно независимы.")
