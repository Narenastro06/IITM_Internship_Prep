# Problem 14: Calculate the shear stress on a shaft.
# Torque T = 500 Nm, radius r = 0.03 m, polar moment J = 1.27e-6 m⁴
# Formula: shear_stress = (T * r) / J
# Print shear stress in MPa with 2 decimal places.

T = 500 #Torque of shaft in Nm
r = 0.03 #Radius of shaft in m
J = 1.27e-6 #Polar moment in m⁴
shear_stress = (T*r)/J
print(f"Shear stress on the shaft is: {shear_stress/1e6:.2f} MPa")