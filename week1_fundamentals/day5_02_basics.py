#Problem 51: stress_values = [120, 250, 180, 300, 95, 210, 175, 340, 160, 220]
# Print only values above 200 MPa

stress_values = [120, 250, 180, 300, 95, 210, 175, 340, 160, 220]
for stress in stress_values:
    if stress > 200:
        print(f"The stress are: {stress} MPa")

# Same list
# Count how many values are below 200 MPa

count = 0
stress_values = [120, 250, 180, 300, 95, 210, 175, 340, 160, 220]
for stress in stress_values:
    if stress < 200:
        count = count + 1
print(count)


# Same list
# Multiply every value by 1.5 (safety factor)
# Print each new value

stress_values = [120, 250, 180, 300, 95, 210, 175, 340, 160, 220]
for stress in stress_values:
    stress = stress*1.5
    print(stress)