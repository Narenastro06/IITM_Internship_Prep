#Problem 18: Calculate Reynolds number (density=1000, velocity=2.5, diameter=0.05, viscosity=0.001)
#Print Re value. Print flow regime using if/elif/else

density = 1000 #in kg/m³
velocity = 2.5 #in m/s
diameter = 0.05 #in m
viscosity = 0.001 #Pa-s

Re = (density*velocity*diameter)/viscosity #Reylond's number in unitless
if Re < 2000:
    print(f"Reynolds Number: {Re:.2f}")
    print("Flow Regime: Laminar Flow")
elif 2000 <= Re <= 4000:
    print(f"Reynolds Number: {Re:.2f}")
    print("Flow Regime: Transitional Flow")
else:
    print(f"Reynolds Number: {Re:.2f}")
    print("Flow Regime: Turbulent Flow")