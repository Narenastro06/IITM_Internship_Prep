# Problem 16: Calculate velocity in a pipe.
# Pipe diameter = 0.08 m, flow rate Q = 0.01 m³/s
# Formula: Area = π * r², velocity = Q / Area
# Then calculate Reynolds number (density = 1000, viscosity = 0.001)
# Print area, velocity and Re — all clean with 2 decimal places. 

diameter = 0.08 #Diameter of pipe
Q = 0.01 #Flow rate of the liquid in pipe in m³/s
radius = diameter/2 #Radius of pipe in m
density = 1000 #Density of the liquid in kg/m³
area = 3.14*radius**2 #Area of the pipe m²
viscosity = 0.001 #viscosity of the fluid Pa-s
print(f"The area of the pipe is: {area:.2e} m²")


velocity = Q/area #Velocity of the liquid 

print(f"The velocity of the liquid is: {velocity:.2f} m/s")

Re = (density*velocity*diameter)/viscosity #Reylond's number with no unit

print(f"The Reylond's number is: {Re:.2f}")