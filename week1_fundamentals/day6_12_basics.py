# Problem 62: You have a list of forces and a fixed area
# forces = [1000, 2000, 3000, 4000, 5000] N
# area = 0.001 m²
# Calculate shear stress for each force using a function
# Print each force and its shear stress in MPa

def shear_stress(force, area):
    for i in range(len(force)):
        shear_stress = force[i]/area
        print(f"Force: {force[i]} N - Shear Stress: {shear_stress/1e6} MPa")
    return shear_stress
force = [1000, 2000, 3000, 4000, 5000] #in N
area = 0.001 #m²
shear_stress = shear_stress(force, 0.001)
