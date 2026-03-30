# Problem 59: Write a function called beam_deflection
# Takes: force, length, E, I
# Formula: deflection = (force * length^3) / (3 * E * I)
# While force increases by 100N each step
# Stop when deflection exceeds 5mm (0.005m)
# Return final force and deflection
# Call it: beam_deflection(100, 1.0, 200e9, 1e-6)
# Print: "Force: X N - Deflection: X mm"

def beam_deflection (force, length, E, I):
    deflection = (force*length**3)/(3*E*I)
    while deflection < 0.005:
        force = force + 100 #increase by 100N
        deflection = (force*length**3)/(3*E*I)
    return force, deflection
force, deflection = beam_deflection(100, 1.0, 200e9, 1e-6)
print(f"Force {force} N, Deflection {deflection} mm")