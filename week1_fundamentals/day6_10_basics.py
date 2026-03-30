# Problem 60: Write a function called thermal_stress
# Takes: E, alpha, temp_change
# Formula: thermal_stress = E * alpha * temp_change
# While temp_change increases by 10 each step
# Stop when thermal_stress exceeds 100 MPa
# E = 200e9, alpha = 12e-6 for steel
# Return final temp_change and thermal_stress
# Call it: thermal_stress(200e9, 12e-6, 10)
# Print: "Temp change: X°C - Thermal Stress: X MPa"

def thermal_stress(E, alpha, temp_change):
    thermal_stress = E*alpha*temp_change
    while thermal_stress < 100e6:
        temp_change = temp_change + 0.1 
        thermal_stress = E*alpha*temp_change
        if thermal_stress > 100e6:  # check after calculating
            break                   # stop immediately
    return temp_change, thermal_stress
temp_change, thermal_stress = thermal_stress(200e9, 12e-6, 10)
print(f"Temp change: {temp_change}°C - Thermal Stress: {thermal_stress/1e6} MPa")