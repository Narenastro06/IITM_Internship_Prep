#Power law describes how viscosity changes at 
#different shear rates for Non-Newtonian fluids.

import numpy as np

shear_rate = np.array([0.1, 1.0, 10.0, 100.0, 1000.0])
K = 2.5   # consistency index — how thick the fluid is overall
n = 0.4   # flow behaviour index — n < 1 means shear thinning (CMC, blood, ketchup)
viscosity = K*shear_rate**(n-1)
print(f"Shear Rate: {shear_rate}")
print(f"Viscosity: {viscosity}")
