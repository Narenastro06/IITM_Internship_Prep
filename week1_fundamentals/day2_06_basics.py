material = "Titanium"
E = 116e9 #Pa
stress = 250e6 #Pa
density = 4500 #kg/m³
print(f"The given material is: {material}")
print(f"Young's modulus of the given material is: {E/1e9:.2f} GPa")
print(f"Stress exerted on the given material is: {stress/1e6:.2f} MPa")
print(f"Density of the given material is: {density:.2f} kg/m³")