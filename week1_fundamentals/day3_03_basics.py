# Problem 19: A beam is under bending stress. E = 200 GPa, stress = 180 MPa, yield_stress = 250 MPa.
# Calculate strain = stress / E. Print stress, strain, and safety verdict:
# stress > yield_stress → FAILURE 
# stress > 0.8 * yield_stress → WARNING
# else → SAFE

E = 200e9 #in Pa
stress = 180e6 #in Pa
yield_stress = 250e6 #in Pa
strain = stress/E #No unit
print(f"Young's modulus for the given body is: {E/1e9:.2f} GPa")
print(f"Stress: {stress/1e6:.2f} MPa")
print(f"Yield Stress: {yield_stress/1e6:.2f} MPa")
print(f"The strain acting on the body is: {strain:.4f}")

if stress > yield_stress:
    print("FAILURE")
elif stress > 0.8*yield_stress:
    print("WARNING")
else:
    print("SAFE")