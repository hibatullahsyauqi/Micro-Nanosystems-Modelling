import math
import numpy as np

# Функция для вычисления координаты x
def calculate_x(alpha, beta):
  return alpha * (math.tan(beta) / (math.tan(beta) - math.tan(alpha)))

# Функция для вычисления координаты y
def calculate_y(alpha, beta):
  return alpha * (math.tan(alpha) * math.tan(beta) / (math.tan(beta) - math.tan(alpha)))

# Известные угловые параметры
alpha_9 = np.deg2rad(54.80)
beta_9 = np.deg2rad(65.59)
alpha_10 = np.deg2rad(54.06)
beta_10 = np.deg2rad(64.59)

# Расстояние между станциями составляет 500 метров
distance_a = 500

# Вычисляем координаты x и y в моменты времени t = 9 с и t = 10 с
x_9 = calculate_x(alpha_9, beta_9)
y_9 = calculate_y(alpha_9, beta_9)
x_10 = calculate_x(alpha_10, beta_10)
y_10 = calculate_y(alpha_10, beta_10)

# Вычисляем изменение x и y между моментами времени t = 9 с и t = 10 с
delta_x = distance_a + (x_10 - x_9)
delta_y = y_10 - y_9

# Приблизительная горизонтальная скорость (v_x) в момент t = 10 с с использованием численного дифференцирования
v_x = delta_x / 1  # 1 - интервал времени между показаниями (с)

# Приблизительная вертикальная скорость (v_y) в момент t = 10 с с использованием численного дифференцирования
v_y = delta_y / 1

# Вычисляем общую скорость (v) с помощью теоремы Пифагора
v = math.sqrt(v_x**2 + v_y**2)

# Вычисляем угол взлета (gamma) в момент t = 10 с с использованием арктангенса
gamma = math.degrees(math.atan(v_y / v_x))

# Выводим результаты
print("Приблизительная скорость (v) в момент t = 10 с:", v, "м/с")
print("Приблизительный угол взлета (gamma) в момент t = 10 с:", gamma, "градусов")
