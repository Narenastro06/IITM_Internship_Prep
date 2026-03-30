# Problem 63: You have a list of pipe diameters
# diameters = [0.01, 0.02, 0.03, 0.04, 0.05] m
# velocity = 2.0, density = 1000, viscosity = 0.001
# Use your reynolds_number function
# Print each diameter, Re, and flow type
def reynolds_number(velocity, density, viscosity, diameter):
    re = (density*velocity*diameter)/viscosity
    if re > 4000:
        flow = "TURBULENT"
    elif 2300 <= re <= 4000:
        flow = "MIXTURE"
    else:
        flow = "LAMINAR"
    return re, flow
    
diameters = [0.01, 0.02, 0.03, 0.04, 0.05] #in m  
velocity = 2.0
density = 1000
viscosity = 0.001
for i in range(len(diameters)):
    re, flow = reynolds_number(velocity, density, viscosity, diameters[i])  # CORRECT
    print(f"Diameter: {diameters[i]} m - Re: {re} - {flow}")

