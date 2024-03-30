import numpy as np

A = np.array([[2, -3, -1],
              [3, 2, -5],
              [2, 4, 1]])
X = np.array([-0.13333333333333308, -1.4666666666666666, 1.1333333333333333])
B = np.array([3, -9, -5])

AX = np.dot(A, X)
print("A * X =", AX)
print("B =", B)