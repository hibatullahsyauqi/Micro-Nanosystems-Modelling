import numpy as np
import matplotlib.pyplot as plt

# Crank length
R = 0.09  # m

# Theta values for which to calculate acceleration
theta_deg = np.linspace(0, 180, 37)  # 37 points from 0 to 180 degrees
theta_rad = np.deg2rad(theta_deg)

# Function to calculate piston position
def x(theta):
    return R * (np.cos(theta) + np.sqrt(2.5**2 - (np.sin(theta))**2))

# Function to calculate velocity using central difference method
def velocity(f, theta, dt):
    return (f(theta + dt) - f(theta - dt)) / (2 * dt)

# Function to calculate acceleration using central difference method
def acceleration(f, theta, dt):
    return (velocity(f, theta + dt, dt) - velocity(f, theta - dt, dt)) / (2 * dt)

# Recursive function to calculate dt values and plot acceleration vs theta
def recursive_dt(dt_values):
    if len(dt_values) == 0:
        return
    dt = dt_values[0]
    a_vals = [acceleration(x, theta, dt) for theta in theta_rad]
    plt.plot(theta_deg, a_vals, label=f'dt = {dt}')
    recursive_dt(dt_values[1:])

# List of dt values
dt_values = [0, 5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180]

# Call the recursive function
recursive_dt(dt_values)

# Add legend and labels to the plot
plt.legend()
plt.xlabel("Theta (degrees)")
plt.ylabel("Acceleration (m/s^2)")
plt.title("Acceleration of piston vs crank angle")
plt.grid(True)
plt.show()