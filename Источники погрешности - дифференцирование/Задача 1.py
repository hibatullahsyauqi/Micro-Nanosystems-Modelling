import numpy as np
import matplotlib.pyplot as plt

# Crank length
R = 0.09  # m

# Constant angular speed
d0_dt = 5000 * 2 * np.pi  # rad/s (convert rpm to rad/s)

# Theta values for which to calculate acceleration
theta_deg = np.linspace(0, 180, 37)  # 37 points from 0 to 180 degrees
theta_rad = np.deg2rad(theta_deg)

# Function to calculate piston position
def x(theta):
    return R * (np.cos(theta) + np.sqrt(2.5^2-(np.sin(theta))^2)

# Calculate position at each theta value
x_vals = x(theta_rad)

# Function to calculate velocity using central difference method
def velocity(f, theta, dt):
    return (f(theta + dt) - f(theta - dt)) / (2 * dt)

# Calculate velocity at each theta value
v_vals = velocity(x, theta_rad, 0.001)  # dt = 0.001 radians

# Function to calculate acceleration using central difference method
def acceleration(f, theta, dt):
    return (velocity(f, theta + dt, dt) - velocity(f, theta - dt, dt)) / (2 * dt)

# Calculate acceleration at each theta value
a_vals = acceleration(x, theta_rad, 0.001)  # dt = 0.001 radians

# Plot acceleration vs theta
plt.plot(theta_deg, a_vals)
plt.xlabel("Theta (degrees)")
plt.ylabel("Acceleration (m/s^2)")
plt.title("Acceleration of piston vs crank angle")
plt.grid(True)
plt.show()