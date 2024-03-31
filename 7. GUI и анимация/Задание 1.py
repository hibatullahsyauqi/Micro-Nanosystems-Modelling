import tkinter as tk
import numpy as np
import matplotlib.backends.backend_tkagg as tkagg
from matplotlib.figure import Figure
# Переменные
t = 0
num_points = 1000
x_sin = np.sin(2 * np.pi * t)
x_cos = np.cos(2 * np.pi * t)
animation_running = False
# Функция
def animate():
    global t, x_sin, x_cos, animation_running
    if animation_running:
        # Обновление времени и значений функций
        t += 0.01
        x_sin = np.sin(2 * np.pi * t)
        x_cos = np.cos(2 * np.pi * t)
        # Очистка графика
        ax.clear()
        # Построение синуса и косинуса
        ax.plot(np.linspace(0, t, num_points), np.sin(2 * np.pi * np.linspace(0, t, num_points)), label="Sin", color="magenta")
        ax.plot(np.linspace(0, t, num_points), np.cos(2 * np.pi * np.linspace(0, t, num_points)), label="Cos", color="salmon")
        ax.legend()
        canvas.draw()
        # Продолжение кадров по времени
        window.after(1, animate)
# Функция переключения состояния
def toggle_animation():
    global animation_running
    if animation_running:
        animation_running = False
        button.config(text="Начать анимацию")
    else:
        animation_running = True
        button.config(text="Приостановить анимацию")
        animate()
# Создание главного окна
window = tk.Tk()
window.title("Гармонические колебания")
# Создание холста для графика
fig = Figure(figsize=(6, 4), dpi=100)
canvas = tkagg.FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
# Создание графика
ax = fig.add_subplot(111)
ax.plot(np.linspace(0, t, num_points), np.sin(2 * np.pi * np.linspace(0, t, num_points)), label="Sin", color="magenta")
ax.plot(np.linspace(0, t, num_points), np.cos(2 * np.pi * np.linspace(0, t, num_points)), label="Cos", color="salmon")
ax.legend()
# Создание кнопки start/pause
button = tk.Button(window, text="Начать анимацию", command=toggle_animation)
button.pack()
# Запуск цикла
window.mainloop()
