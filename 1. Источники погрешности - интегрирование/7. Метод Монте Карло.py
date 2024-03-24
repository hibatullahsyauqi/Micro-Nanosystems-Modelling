import math
import numpy as np

N = 10
a = 0
b = 1
real = math.exp(1) - 1

def f(x):
    return math.exp(x)

for j in range(9):
    sum = 0.0
    h = (b-a)/N
    for i in range(N):
        x = a + (b-a)*np.random.uniform()
        sum += f(x)
    sum *= h
    error = abs(real - sum)
    print('integral: ', sum, '\th: ', h, '\terror: ', error)
    N *= 10