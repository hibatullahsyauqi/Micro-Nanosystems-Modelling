import numpy as np
import matplotlib.pyplot as plt
# Заданные параметры
L = 100e-6
T0 = 300
T_nagr = 600
T_center_desired = 450
alpha = 1.68e-7
# Шаг по пространству (м)
h = 1e-6
# Шаг по времени (с)
tau = (h ** 2) / (2 * alpha)
N = int(L / h) + 1
T = np.ones(N) * T0
T[-1] = T_nagr
time = 0
while True:
    time += tau
    T[1:N-1] += alpha * tau / h ** 2 * (T[2:N] - 2 * T[1:N-1] + T[:N-2])
    if T[N // 2] >= T_center_desired:
        break
print("Время, за которое центр стержня нагреется до {} K: {:.2f} с".format(T_center_desired, time))
# Визуализация
plt.plot(np.linspace(0, L, N), T)
plt.xlabel('Расстояние (м)')
plt.ylabel('Температура (K)')
plt.title('Распределение температур по длине балки')
plt.grid(True)
plt.show()