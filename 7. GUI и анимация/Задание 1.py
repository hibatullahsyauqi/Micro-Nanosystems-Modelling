import tkinter as tk
import numpy as np
import matplotlib.backends.backend_tkagg as tkagg
from matplotlib.figure import Figure

# Функция для анимации
def animate():
    global t, x_sin, x_cos

    # Обновление значений времени
    t += 0.01

    # Вычисление значений синуса и косинуса
    x_sin = np.sin(2 * np.pi * t)
    x_cos = np.cos(2 * np.pi * t)

    # Очистка графика
    ax.clear()

    # Отрисовка графика
    ax.plot(np.linspace(0, t, num_points), np.sin(2 * np.pi * np.linspace(0, t, num_points)), label="Sin", color="magenta")
    ax.plot(np.linspace(0, t, num_points), np.cos(2 * np.pi * np.linspace(0, t, num_points)), label="Cos", color="salmon")

    # Настройка легенды
    ax.legend()

    # Обновление канваса
    canvas.draw()

    # Запуск следующего кадра анимации
    window.after(1, animate)

# Инициализация
t = 0
num_points = 1000

# Создание окна
window = tk.Tk()
window.title("Анимация гармонических колебаний")

# Создание холста
fig = Figure(figsize=(6, 4), dpi=100)
canvas = tkagg.FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Создание графика
ax = fig.add_subplot(111)
ax.plot(np.linspace(0, t, num_points), np.sin(2 * np.pi * np.linspace(0, t, num_points)), label="Sin", color="magenta")
ax.plot(np.linspace(0, t, num_points), np.cos(2 * np.pi * np.linspace(0, t, num_points)), label="Cos", color="salmon")
ax.legend()

# Создание кнопки
button = tk.Button(window, text="Start animation", command=animate)
button.pack()

# Запуск главного цикла
window.mainloop()