import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# Данные
m = [10, 4, 5, 6]
mu = [0.25, 0.3, 0.2]
theta = 45 * np.pi / 180
g = 9.82
b = [m[i] * g * (np.sin(theta) - mu[i] * np.cos(theta)) for i in range(len(mu))]
b = np.append(b, -m[3] * g)
a = np.array([[1, 0, 0, m[0]], [-1, 1, 0, m[1]], [0, -1, 1, m[2]], [0, 0, -1, m[3]]])
# Решение системы уравнений
X = np.linalg.solve(a, b)
print(f"Ответ системы уравнений:\n{X}\n")
# Время для анимации
t_animation = np.linspace(0, 50, 100)
# Уравнение движения
def r_t(t):
    return 100 + X[3] * t + 0.5 * t**2 * X[2]
# Создание анимации
fig, ax = plt.subplots()
ax.set_xlim(0, 5)  # Устанавливаем пределы оси x
ax.set_ylim(0, 1000)  # Устанавливаем пределы оси y
line, = ax.plot([], [], color='red')
def update(frame):
    x = t_animation[:frame]
    y = r_t(t_animation[:frame])
    line.set_data(x, y)
    return line,
ani = FuncAnimation(fig, update, frames=len(t_animation), blit=True)
plt.xlabel('Время (с)')
plt.ylabel('Расстояние (м)')
plt.title('Движение системы')
plt.grid(True)
plt.show()
