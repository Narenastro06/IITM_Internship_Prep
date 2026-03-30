material = {
    "steel" : {"E": 200e9, "yield_stress": 250e6, "density": 7850},
    "aluminium" : {"E": 69e9, "yield_stress": 270e6, "density": 2700},
    "titanium" : {"E": 116e9, "yield_stress": 880e6, "density": 4500}
}

for i in material:
    print(f"{i} E: {material[i]['E']/1e9} GPa, Yield: {material[i]['yield_stress']/1e6} MPa, Density: {material[i]['density']} kg/m³")