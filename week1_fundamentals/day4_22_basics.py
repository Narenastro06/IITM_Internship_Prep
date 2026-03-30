#Problem 45: Start with strain = 0.0
# Increase by 0.001 each loop
# E = 200e9 Pa
# Formula: stress = E * strain
# Stop when stress exceeds 250 MPa (250e6 Pa)
# Print each strain and stress value

strain = 0.0
E = 200e9 #in Pa
stress = 0
while stress < 250e6:
    stress = E*strain
    print(f"The stress is: {stress/1e6} in MPa")
    strain = strain + 0.001
