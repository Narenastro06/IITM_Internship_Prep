# Problem 12: A steel sample is tested in a lab. 
# Store E = 200 GPa, stress = 400 MPa, density = 7850 kg/m³, strain = 0.002 in base SI units. 
# Calculate E verification = stress / strain. 
# Print a clean material report using f-strings with 2 decimal places and correct units.

material ="Steel"
stress = 400e6 #in Pa
strain = 0.002 #no unit
density = 7850 #in kg/m³
E = 200e9 #in GPa
E_verify = stress/strain

print(f"The material is: {material}")
print(f"Stress exerted on the given material is: {stress/1e6:.2f} MPa")
print(f"Strain exerted on the given material is: {strain}")
print(f"Density of the given material is: {density:.2f} kg/m³")
print(f"The verification of the given E value is {E_verify/1e9:.2f} GPa")
print(f"The Young's modulus for the given material is {E/1e9:.2f} GPa")