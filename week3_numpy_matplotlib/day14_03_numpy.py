import numpy as np
strain = np.array([0.001, 0.002, 0.003, 0.004, 0.005])
E = 200e9
stress = E*strain
print(f"Strain: {strain}")
print(f"Stress: {stress/1e6} MPa")
