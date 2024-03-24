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
        ya = (5/9)*f(((h*i/2)*(-math.sqrt(3)/math.sqrt(5)))+((b+a)/2))
        yb = (8/9)*f(((h*i/2)*0)+((b+a)/2))
        yc = (5/9)*f(((h*i/2)*(math.sqrt(3)/math.sqrt(5)))+((b+a)/2))
        sum += (ya+yb+yc)*h/2
        error = real - sum
    print(f'integral: ', sum, '\th: ', h, '\terror: ', error)
    N *= 10
    