# Problem 21: Fluid is flowing through two different pipes in a system.
# Pipe 1: diameter = 0.05 m, velocity = 3 m/s
# Pipe 2: diameter = 0.08 m, velocity = ?
# Continuity equation: A1 * V1 = A2 * V2
# density = 1000 kg/m³, viscosity = 0.001 Pa·s
#
# Calculate:
# 1. Area of both pipes
# 2. Velocity in Pipe 2 using continuity equation
# 3. Reynolds number for BOTH pipes
# 4. Print flow regime for BOTH pipes
# 5. Print which pipe has higher Re and by how much (difference)

# density = 1000 kg/m³, viscosity = 0.001 Pa·s
d1 = 0.05 #Diameter of pipe 1 in m
d2 = 0.08 #Diameter of pipe 2 in m
v1 = 3 #Velocity in m/s
density = 1000 #kg/m³
viscosity = 0.001 #in Pa·s
print(f"Diameter of pipe 1 is: {d1} m")
print(f"Diameter of pipe 2 is: {d2} m")
print(f"Velocity of fluid in pipe 1 is: {v1} m/s")
print(f"Density of the fluid is: {density} kg/m³")
print(f"Viscosity of the fluid is: {viscosity} Pa·s")
# From continuity equation: A1 * V1 = A2 * V2

#01. Calculating area of both pipes
A1 = (3.14/4)*(d1**2) #Area of pipe 1
print(f"Area of pipe 1 is: {A1:.4f} m²")
A2 = (3.14/4)*(d2**2) #Area of pipe 2
print(f"Area of pipe 2 is: {A2:.4f} m²")

#02. Velocity in Pipe 2 using continuity equation
v2 = (A1*v1)/A2 
print(f"Velocity in Pipe 2 using continuity equation is: {v2:.2f} m/s")

#03. Reynolds number for BOTH pipes
Re1 = (v1*d1*density)/viscosity #Reynolds number for pipe 1, unitless
print(f"Reynolds number for pipe 1 is: {Re1:.2f}")
Re2 = (v2*d2*density)/viscosity #Reynolds number for pipe 2, unitless
print(f"Reynolds number for pipe 2 is: {Re2:.2f}")

#04. Print flow regime for BOTH pipes
# Pipe 1 flow regime
if Re1 > 4000:
    print("The flow in pipe 1 is TURBULENT FLOW")
elif 2000 <= Re1 <= 4000:
    print("The flow in pipe 1 is MIXED FLOW")
elif Re1 < 2000:
    print("The flow in pipe 1 is LAMINAR FLOW")

# Pipe 2 flow regime
if Re2 > 4000:
    print("The flow in pipe 2 is TURBULENT FLOW")
elif 2000 <= Re2 <= 4000:
    print("The flow in pipe 2 is MIXED FLOW")
elif Re2 < 2000:
    print("The flow in pipe 2 is LAMINAR FLOW")

#05. Print which pipe has higher Re and by how much (difference)
if Re1 > Re2:
    print("Reynolds number 1 is greater than Reynolds number 2")
    print(f"The difference is {Re1 - Re2:.2f}")
else:
     print("Reynolds number 2 is greater than Reynolds number 1")
     print(f"The difference is {Re2 - Re1:.2f}")