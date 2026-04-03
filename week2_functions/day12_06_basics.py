file = open("real_viscosity.txt","r")
lines = file.readlines()
file.close()

output = open("real_results.txt", "w")
output.write("shear_rate,viscosity,shear_stress\n")

for line in lines[2:]:
    values = line.strip().split(",")
    shear_rate = float(values[0])
    viscosity = float(values[1])
    shear_stress = viscosity*shear_rate
    output.write(f"{shear_rate},{viscosity},{shear_stress}\n")
    print(f"Shear Rate: {shear_rate} - Viscosity: {viscosity} - Shear Stress: {shear_stress}")
output.close()
print("Results saved to real_results.txt") 