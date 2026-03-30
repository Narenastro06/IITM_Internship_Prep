# Problem 13: A fluid flows through a pipe. \
# Calculate Reynolds number where the density = 1000 kg/m³, velocity = 2.5 m/s, 
# diameter = 0.05 m, viscosity = 0.001 Pa·s. # Formula: Re = (density * velocity * diameter) / viscosity. 
# Print Re with 2 decimal places. 

density = 1000 #kg/m³
velocity = 2.5 #m/s 
diameter = 0.05 #m 
viscosity = 0.001 #Pa·s
Re = (density*velocity*diameter)/viscosity #Re is Reylond's number with no unit
print(f"The Reylond's number is: {Re:.2f}") 