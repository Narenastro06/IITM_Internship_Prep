# You have this material dictionary.
# Task:
# 1. Add a new material — copper: E=110 GPa, yield_stress=210 MPa, density=8960
# 2. Loop through all materials
# 3. Print each material's name and its specific strength
#    Specific strength = yield_stress / density
# 4. Print which material has the HIGHEST specific strength

material = {
    "steel" : {"E": 200e9, "yield_stress": 250e6, "density": 7850},
    "aluminium" : {"E": 69e9, "yield_stress": 270e6, "density": 2700},
    "titanium" : {"E": 116e9, "yield_stress": 880e6, "density": 4500}
}

# 1. Add a new material — copper: E=110 GPa, yield_stress=210 MPa, density=8960
material["copper"] = {"E": 110e9, "yield_stress": 210e6, "density": 8960}

# 2. Loop through all materials
for i in material:
    print(f"{i} E: {material[i]['E']/1e9} GPa, Yield: {material[i]['yield_stress']/1e6} MPa, Density: {material[i]['density']} kg/m³" )

# 3. Print each material's name and its specific strength
#    Specific strength = yield_stress / density
for i in material:
    specific_strength = material[i]["yield_stress"]/material[i]["density"]
    print(f"The specific strength of the given material is: {specific_strength}")

# 4. Print which material has the HIGHEST specific strength
highest_specific_strength = 0
strongest_material = ""
for i in material:
    specific_strength = material[i]["yield_stress"] / material[i]["density"]
    if specific_strength>highest_specific_strength:
        highest_specific_strength = specific_strength
        strongest_material = i
print(f"Strongest material: {strongest_material}, Specific strength: {highest_specific_strength}")