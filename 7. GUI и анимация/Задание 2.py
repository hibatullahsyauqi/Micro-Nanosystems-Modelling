import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.backends.backend_tkagg as tkagg
from matplotlib.figure import Figure
# Переменные
t = 0
num_points = 1000
amplitude_sin = 1.0
amplitude_cos = 1.0
phase_sin = 0.0
phase_cos = 0.0
frequency_sin = 1.0
frequency_cos = 1.0
noise_amplitude = 0.0
animation_running = False
# Функция
def animate():
    global t, animation_running
    if animation_running:
        t += 0.01
        t_values = np.linspace(0, t, num_points)  # Генерация массива t_values
        # Создание новых массивов x_sin и x_cos
        x_sin = amplitude_sin * np.sin(2 * np.pi * frequency_sin * t_values + phase_sin)
        x_cos = amplitude_cos * np.cos(2 * np.pi * frequency_cos * t_values + phase_cos)
        if noise_amplitude != 0.0:
            noise = noise_amplitude * np.random.randn(num_points)
            x_sin += noise
            x_cos += noise
        # Очистка графика
        ax.clear()
        # Если амплитуда шума равна нулю, просто используем синус и косинус без добавления шума
        if noise_amplitude == 0.0:
            ax.plot(t_values, amplitude_sin * np.sin(2 * np.pi * frequency_sin * t_values + phase_sin), label="Sin", color="magenta")
            ax.plot(t_values, amplitude_cos * np.cos(2 * np.pi * frequency_cos * t_values + phase_cos), label="Cos", color="salmon")
        else:
            # Построение синуса и косинуса с добавлением шума
            ax.plot(t_values, x_sin, label="Sin", color="magenta")
            ax.plot(t_values, x_cos, label="Cos", color="salmon")
        ax.legend()
        canvas.draw()
        window.after(1, animate)
# Функции для изменения параметров        
def update_sin_params(event):
    global amplitude_sin, phase_sin, frequency_sin
    amplitude_sin = sin_amp_scale.get()
    phase_sin = sin_phase_scale.get()
    frequency_sin = sin_freq_scale.get()
    animate()
def update_cos_params(event):
    global amplitude_cos, phase_cos, frequency_cos
    amplitude_cos = cos_amp_scale.get()
    phase_cos = cos_phase_scale.get()
    frequency_cos = cos_freq_scale.get()
    animate()
def update_noise_amplitude(event):
    global noise_amplitude
    noise_amplitude = noise_scale.get()
    animate()
# Функция для переключения состояния анимации
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
window.title("Гармонические колебания с Гауссовым шумом")
# Создание холста для графика
fig = Figure(figsize=(6, 4), dpi=100)
canvas = tkagg.FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
# Создание графика
ax = fig.add_subplot(111)
ax.plot(np.linspace(0, t, num_points), amplitude_sin * np.sin(2 * np.pi * frequency_sin * np.linspace(0, t, num_points) + phase_sin), label="Sin", color="magenta")
ax.plot(np.linspace(0, t, num_points), amplitude_cos * np.cos(2 * np.pi * frequency_cos * np.linspace(0, t, num_points) + phase_cos), label="Cos", color="salmon")
ax.legend()
# Создание кнопки start/pause
button = tk.Button(window, text="Начать анимацию", command=toggle_animation)
button.pack()
# Создание помещений для слайдеров
sin_frame = ttk.Frame(window)
sin_frame.pack(side=tk.LEFT, padx=10, pady=10)
cos_frame = ttk.Frame(window)
cos_frame.pack(side=tk.LEFT, padx=10, pady=10)
noise_frame = ttk.Frame(window)
noise_frame.pack(side=tk.LEFT, padx=10, pady=10)
# Создание слайдеров для амплитуды синуса
sin_amp_label = tk.Label(sin_frame, text="Амплитуда синуса")
sin_amp_label.pack()
sin_amp_scale = ttk.Scale(sin_frame, from_=0.1, to=2.0, length=200, orient="horizontal")
sin_amp_scale.pack()
sin_amp_scale.bind("<ButtonRelease-1>", update_sin_params)
# Создание слайдеров для фазы синуса
sin_phase_label = tk.Label(sin_frame, text="Фаза синуса")
sin_phase_label.pack()
sin_phase_scale = ttk.Scale(sin_frame, from_=0.0, to=2*np.pi, length=200, orient="horizontal")
sin_phase_scale.pack()
sin_phase_scale.bind("<ButtonRelease-1>", update_sin_params)
# Создание слайдеров для частоты синуса
sin_freq_label = tk.Label(sin_frame, text="Частота синуса")
sin_freq_label.pack()
sin_freq_scale = ttk.Scale(sin_frame, from_=0.1, to=2.0, length=200, orient="horizontal")
sin_freq_scale.pack()
sin_freq_scale.bind("<ButtonRelease-1>", update_sin_params)
# Создание слайдеров для амплитуды косинуса
cos_amp_label = tk.Label(cos_frame, text="Амплитуда косинуса")
cos_amp_label.pack()
cos_amp_scale = ttk.Scale(cos_frame, from_=0.1, to=2.0, length=200, orient="horizontal")
cos_amp_scale.pack()
cos_amp_scale.bind("<ButtonRelease-1>", update_cos_params)
# Создание слайдеров для фазы косинуса
cos_phase_label = tk.Label(cos_frame, text="Фаза косинуса")
cos_phase_label.pack()
cos_phase_scale = ttk.Scale(cos_frame, from_=0.0, to=2*np.pi, length=200, orient="horizontal")
cos_phase_scale.pack()
cos_phase_scale.bind("<ButtonRelease-1>", update_cos_params)
# Создание слайдеров для частоты косинуса
cos_freq_label = tk.Label(cos_frame, text="Частота косинуса")
cos_freq_label.pack()
cos_freq_scale = ttk.Scale(cos_frame, from_=0.1, to=2.0, length=200, orient="horizontal")
cos_freq_scale.pack()
cos_freq_scale.bind("<ButtonRelease-1>", update_cos_params)
# Создание слайдера для амплитуды шума
noise_label = tk.Label(noise_frame, text="Амплитуда шума")
noise_label.pack()
noise_scale = ttk.Scale(noise_frame, from_=0.0, to=1.0, length=200, orient="horizontal")
noise_scale.pack()
noise_scale.bind("<ButtonRelease-1>", update_noise_amplitude)
# Запуск цикла
window.mainloop()