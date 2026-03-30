# Problem 57: Write a function called shear_stress
# Takes: force, area
# Formula: shear_stress = force / area
# While force increases by 500N each step
# Stop when shear_stress exceeds 50 MPa
# Return final force and shear_stress
# Call it: shear_stress(500, 0.001)
# Print: "Force: X N - Shear Stress: X MPa"

def shear_stress(force, area):
    shear_stress = force/area 
    while shear_stress < 50e6:
        force = force + 500 #increases by 500N
        shear_stress = force/area 
    return force, shear_stress
final_force, final_stress = shear_stress(500, 0.001)
print(f"Force {final_force} N - Shearstress {final_stress/1e6} MPa")