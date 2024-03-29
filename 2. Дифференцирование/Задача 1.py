import numpy as np
import matplotlib.pyplot as plt

# Длина шатуна
R = 0.09  # м

# Постоянная угловая скорость
d0_dt = 5000 * 2 * np.pi  # рад/с (переводим об/мин в рад/с)

# Значения угла theta, для которых вычисляется ускорение
theta_deg = np.arange(0, 185, 5)
theta_rad = np.deg2rad(theta_deg)

# Функция для вычисления положения поршня
def x(theta):
    return R * (np.cos(theta) + np.sqrt(2.5**2 - (np.sin(theta))**2))

# Вычисляем положение для каждого значения theta
x_vals = x(theta_rad)

# Функция для вычисления скорости с использованием метода центральной разности
def velocity(f, theta, dt):
    return (f(theta + dt) - f(theta - dt)) / (2 * dt)

# Вычисляем скорость для каждого значения theta
v_vals = velocity(x, theta_rad, 0.000001)  # dt = 0.000001 радиан

# Функция для вычисления ускорения с использованием метода центральной разности
def acceleration(f, theta, dt):
    return (velocity(f, theta + dt, dt) - velocity(f, theta - dt, dt)) / (2 * dt)

# Вычисляем ускорение для каждого значения theta
a_vals = acceleration(x, theta_rad, 0.000001)  # dt = 0.000001 радиан

# Строим график ускорения от theta
plt.plot(theta_deg, a_vals)
plt.xlabel("Theta (градусы)")
plt.ylabel("Ускорение (м/с^2)")
plt.title("Ускорение поршня от угла поворота шатуна")
plt.grid(True)
plt.show()