# Problem 1:
# You have pipe diameters = [0.01, 0.02, 0.03, 0.04, 0.05] m
# velocity = 2.0, density = 1000, viscosity = 0.001
# Calculate Reynolds number for each diameter using NumPy
# No loop — one line calculation
# Print which diameters give turbulent flow (Re > 4000)

import numpy as np
pipe_diameters = np.array([0.01, 0.02, 0.03, 0.04, 0.05])
velocity = 2.0
density = 1000
viscosity = 0.001
re = (pipe_diameters*velocity*density)/viscosity
rounded_re = np.round(re, 2)
print(f"Reynold's Numbers are: {rounded_re}")

greater_re = np.where(re>4000)
print(f"Reynolds Numbers: {rounded_re}")
print(f"Turbulent Re values: {re[greater_re]}")
print(f"Turbulent diameters: {pipe_diameters[greater_re]} m")