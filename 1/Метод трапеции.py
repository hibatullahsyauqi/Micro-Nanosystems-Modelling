import math as math
N = 10
a = 0
b = 1
real = math.exp(1) - 1

def f(x):
    return math.exp(x)
for j in range (9):
    sum = 0.0
    h = (b-a)/N
    for i in range (N):
        ya = f(h*i)
        yb = f(h*i+h)
        sum += (ya + yb)*(h/2)
        error = real - sum
    print(f'integral: ', sum, '\th: ', h, '\terror: ', error)
    N *= 10
