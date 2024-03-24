import math as math
N = 10
x = 1
a = 0
b = 0.1
real = math.exp(1)

def f(x):
    return math.exp(x)
for j in range (9):
    h = (b-a)/N
    diff = (f(x + h/2) - f(x - h/2))/h
    for i in range (N):
        error = abs(real - diff)
    print(f'diff: {diff}, h: {h}, error: {error}')
    N *= 10