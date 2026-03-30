# Write a function called reynolds_number
# Takes: diameter, velocity, density, viscosity
# Formula: Re = (density * velocity * diameter) / viscosity
# Returns Re and flow type:
#   Re < 2300 → Laminar
#   Re > 4000 → Turbulent
#   Otherwise → Transitional
# Call it with:
#   diameter=0.05, velocity=2.0, density=1000, viscosity=0.001
# Print: "Re: 100000.0 - Turbulent"

def reynolds_number(diameter, velocity, density, viscosity):
     Re = (density * velocity * diameter) / viscosity
     if Re < 2000:
          return Re, "LAMINAR"
     elif 2300 <= Re <= 4000:
          return Re, "TRANSTIONAL"
     else:
          return Re, "TURBULENT"


diameter=0.05
velocity=2.0
density=1000
viscosity=0.001

Re, flow = reynolds_number(0.05, 2.0, 1000, 0.001)
print(f"The Reynolds Number is {Re} which is {flow}")

