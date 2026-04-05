import numpy as np
shear_rate =  np.array([0.1, 1.0, 10.0, 100.0, 1000.0])
viscosity = np.array([9.25, 2.5, 0.62, 0.15, 0.039])
print(np.max(viscosity))
print(np.min(viscosity))
print(np.mean(viscosity))
print(np.sum(viscosity))

