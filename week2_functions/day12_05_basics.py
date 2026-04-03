file = open("viscosity_data.txt","r")
lines = file.readlines()
file.close()

output = open("shear_stress_result.txt", "w")

for line in lines[2:]:
    values = line.strip().split(",")
    shear_rate = float(values[0])
    viscosity = float(values[1])
    shear_stress = viscosity*shear_rate
    output.write(f"{shear_rate},{viscosity},{shear_stress}\n")

output.close()
print("Result Saved")