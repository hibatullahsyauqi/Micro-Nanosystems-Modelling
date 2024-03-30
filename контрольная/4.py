import numpy as np

def LUdecomp(a):
    a = a.astype(float)
    n = len(a)
    for k in range(n - 1):
        for i in range(k + 1, n):
            if a[i, k] != 0.0:
                lam = a[i, k] / a[k, k]
                a[i, k + 1:n] -= lam * a[k, k + 1:n]
                a[i, k] = lam
    return a

def LUsolve(a, b):
    n = len(a)
    b = b.astype(float)
    # Прямая подстановка
    for k in range(1, n):
        b[k] -= np.dot(a[k, 0:k], b[0:k])
    # Обратная подстановка
    x = np.zeros_like(b)
    x[n - 1] = b[n - 1] / a[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = (b[i] - np.dot(a[i, i + 1:], x[i + 1:])) / a[i, i]
    return x

# Заданные значения жесткостей пружин и соотношений масс
k = np.array([1, 2, 1, 1, 2])
W = np.array([2, 1, 2])

# Создаем матрицу коэффициентов системы уравнений
A = np.array([[k[0]+k[1]+k[2]+k[4], -k[2], -k[4]],
              [-k[2], k[2]+k[3], -k[3]],
              [-k[4], -k[3], k[3]+k[4]]])

# Решаем систему уравнений
solution = LUsolve(LUdecomp(A), W)

# Выводим решение
print("Решение системы уравнений:")
print("x1 =", solution[0])
print("x2 =", solution[1])
print("x3 =", solution[2])
