#Problem 53: Write a function called stress_verdict
# It takes stress as input
# If stress > 250 MPa → return "Critical"
# If stress 150 to 250 MPa → return "Warning"
# If stress below 150 MPa → return "Safe"
# Call it with stress = 300e6, 200e6, 100e6
# Print each verdict

def stress_verdict(stress):
    if stress  > 250e6:
        return "CRITICAL"
    elif stress <= 250e6 and stress >= 150e6:
        return "WARNING"
    else:
        return "SAFE"

print(stress_verdict(300e6))
print(stress_verdict(200e6))
print(stress_verdict(100e6))