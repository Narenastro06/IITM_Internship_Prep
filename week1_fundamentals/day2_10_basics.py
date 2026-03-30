# Problem 15: A cantilever beam has a point load at the end.
# Load P = 2000 N, length L = 1.5 m, breadth b = 0.05 m, depth d = 0.1 m
# Calculate:
# 1. Moment M = P * L
# 2. Section modulus Z = (b * d²) / 6
# 3. Bending stress = M / Z
# Print all 3 values cleanly with correct units.

P = 2000 #Load acting on the cantilever beam in N
L = 1.5 #Length of cantinlever beam in m 
b = 0.05 #Breadth of cantinlever beam in m 
d =  0.1 #Depth of cantinlever beam in m 

M = P * L #Moment acting on the beam
Z = (b*d**2)/6 #Section modulus acting on the beam
Bending_stress = M/Z #Bending stress acting on the beam 

print(f"Moment acting on the beam is: {M:.2f} Nm")
print(f"Section modulus acting on the beam is: {Z:.2e} m³")
print(f"Bending stress acting on the beam is: {Bending_stress/1e6:.2f} MPa")
