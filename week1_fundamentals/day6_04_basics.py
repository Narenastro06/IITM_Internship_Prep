# Problem 54: Use your stress_verdict function
# stress_values = [120e6, 250e6, 180e6, 300e6, 95e6]
# Loop through each stress value
# Print each stress in MPa and its verdict
# Expected output:
# 120.0 MPa - SAFE
# 250.0 MPa - WARNING
# 180.0 MPa - WARNING
# 300.0 MPa - CRITICAL
# 95.0 MPa - SAFE

def stress_verdict(stress):
        if stress > 250e6:
            return "CRITICAL"
        elif 150e6 <= stress <= 250e6:
            return "WARNING"
        else:
            return "SAFE"
stress_values = [120e6, 250e6, 180e6, 300e6, 95e6]
for stress in stress_values:
    verdict = stress_verdict(stress)
    print(f"{stress/1e6} MPa - {verdict}")