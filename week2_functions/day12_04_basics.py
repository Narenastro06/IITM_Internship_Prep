file = open("viscosity_data.txt","r")
lines = file.readlines()
file.close()

for line in lines[2:]:
    values = line.strip().split(",")
    shear_rate = float(values[0])
    viscosity = float(values[1])
    shear_stress = viscosity*shear_rate
    print(f"Shear Rate: {shear_rate} - Viscosity: {viscosity} - Shear Stress: {shear_stress}") 