material = "Steel"
E = 200e9
stress = 400e6

print(f"The given material is: {material}")
print(f"Young's modulus for the given material is: {E/1e9:.2f}GPa")
print(f"Stres exerted on the given material is: {stress/1e6:.2f}MPa")
