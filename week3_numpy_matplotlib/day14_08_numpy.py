import numpy as np
shear_rate = np.linspace(0.1, 1000, 100)
K = 2.5
n = 0.4
viscosity = K*shear_rate**(n-1)
print(f"The first five viscosity value: {viscosity[:5]}")
print(f"The last five viscosity value: {viscosity[-5:]}")