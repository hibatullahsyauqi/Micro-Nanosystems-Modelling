import math
import numpy as np

# Function to calculate x-coordinate (replace with actual equation)
def calculate_x(alpha, beta):
  return alpha * (math.tan(beta) / (math.tan(beta) - math.tan(alpha)))

# Function to calculate y-coordinate (replace with actual equation)
def calculate_y(alpha, beta):
  return alpha * (math.tan(alpha) * math.tan(beta) / (math.tan(beta) - math.tan(alpha)))

# Sample angle readings (replace with actual readings)
alpha_9 = np.deg2rad(54.80)
beta_9 = np.deg2rad(65.59)
alpha_10 = np.deg2rad(54.06)
beta_10 = np.deg2rad(64.59)

# Distance between stations (a) is 500 meters
distance_a = 500

# Calculate x and y coordinates at t = 9s and t = 10s
x_9 = calculate_x(alpha_9, beta_9)
y_9 = calculate_y(alpha_9, beta_9)
x_10 = calculate_x(alpha_10, beta_10)
y_10 = calculate_y(alpha_10, beta_10)

# Calculate change in x and y between t = 9s and t = 10s
delta_x = distance_a + (x_10 - x_9)
delta_y = y_10 - y_9

# Approximate horizontal speed (v_x) at t = 10s using numerical differentiation
v_x = delta_x / 1  # 1 is the time interval between readings (s)

# Approximate vertical speed (v_y) at t = 10s using numerical differentiation
v_y = delta_y / 1

# Calculate total speed (v) using Pythagorean theorem
v = math.sqrt(v_x**2 + v_y**2)

# Calculate climb angle (gamma) at t = 10s using arctangent
gamma = math.degrees(math.atan(v_y / v_x))

# Print the results
print("Approximate speed (v) at t = 10s:", v, "m/s")
print("Approximate climb angle (gamma) at t = 10s:", gamma, "degrees")
