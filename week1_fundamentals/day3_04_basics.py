# Problem 20: A shaft is under shear stress. Torque T = 800 Nm, radius r = 0.04 m, J = 4.02e-6 m⁴
# Shear yield stress = 150 MPa. Calculate shear stress = (T * r) / J
# Print shear stress in MPa. Print verdict: FAILURE, WARNING (>0.8 * shear yield), or SAFE

T = 800 #Nm
r = 0.04 #m
J = 4.02e-6 #m^4
shear_yield_stress = 150e6 #Pa 
shear_stress = (T*r)/J
print(f"The torque acting on the shaft is: {T} Nm")
print(f"The radius of the shaft is: {r} m")
print(f"J is: {J} m^4")
print(f"The shear yield stress acting is: {shear_yield_stress/1e6:.2f} MPa")
print(f"The shear stress acting is: {shear_stress/1e6:.2f} MPa")

if shear_stress > shear_yield_stress:
    print("FAILURE")
elif shear_stress > 0.8*shear_yield_stress:
    print("WARNING")
else:
    print("SAFE")