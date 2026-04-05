# Read real_viscosity.txt
# Calculate shear stress for each row
# Find highest shear stress and which shear rate caused it
# Write summary to results_summary.txt:
# "Highest shear stress: 310.0 at shear rate: 1000.0"

file = open("real_viscosity.txt","r")
lines = file.readlines()
file.close()
highest = 0
highest_shear_rate = 0
for line in lines[2:]:
    values = line.strip().split(",")
    shear_rate = float(values[0])
    viscosity = float(values[1])
    shear_stress = viscosity*shear_rate
    if shear_stress > highest:
        highest = shear_stress
        highest_shear_rate = shear_rate

output = open("results_summary.txt", "w")
output.write(f"Highest shear stress: {highest} at shear rate: {highest_shear_rate}\n")
output.close()
print("Summary saved")