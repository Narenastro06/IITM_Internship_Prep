#Problem 55: Write a function called material_check
# Takes E and strain as inputs
# Calculates stress = E * strain
# Returns BOTH stress and verdict
# Use stress_verdict logic inside
# Call it for Steel: E=200e9, strain=0.002
# Print: "Stress: 400.0 MPa - WARNING"

def stress_verdict(stress):
    if stress > 400e6:
        return "CRITICAL"
    elif 200e6 <= stress <= 400e6:
        return "WARNING"
    else: 
        return "SAFE"
    
def material_check(E, strain):
    stress = E*strain
    verdict = stress_verdict(stress)
    return stress, verdict

stress, verdict = material_check(200e9, 0.002)
print(f"Stress: {stress/1e6} MPa - {verdict}")