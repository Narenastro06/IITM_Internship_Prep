# Problem 17: A pressure vessel has internal pressure = 5 MPa,
# inner radius = 0.5 m, wall thickness = 0.02 m
# Calculate hoop stress = (pressure * radius) / thickness
# Calculate longitudinal stress = (pressure * radius) / (2 * thickness)
# Print both in MPa with 2 decimal places.
# Also print which stress is higher using a simple print statement (no if/else yet)

pressure = 5e6 #in Pa
radius = 0.5 #in m
wall_thickness = 0.02 #in m
hoop_stress = (pressure*radius)/wall_thickness
print(f"The hoop stress acting is: {hoop_stress/1e6:.2f} MPa")
longitudinal_stress = (pressure*radius)/(2*wall_thickness)
print(f"The longitudinal stress acting is: {longitudinal_stress/1e6:.2f} MPa")

print("The hoop stress is higher than longitudinal stress")