# Mini Challenge 3 — Fluid Mechanics
# Reynolds Number determines if flow is laminar or turbulent
# Formula: Re = (density * velocity * diameter) / viscosity

# You have pipe flow data for 4 different fluids:

#fluids    = ["water",  "oil",   "air",    "glycerin"]
#density   = [1000,     900,     1.2,      1260]      # kg/m³
#velocity  = [2.0,      0.5,     15.0,     0.1]       # m/s
#diameter  = [0.05,     0.05,    0.1,      0.05]      # m
#viscosity = [0.001,    0.1,     0.000018, 1.5]       # Pa·s

# Tasks:
# 1. Calculate Reynolds number for each fluid
# 2. Print fluid name, Re value, and flow type:
#    Re < 2300         → Laminar
#    2300 to 4000      → Transitional
#    Above 4000        → Turbulent
# 3. Count how many are turbulent
# 4. Print which fluid has the highest Reynolds number

pipes = {
    "water":    {"density": 1000, "velocity": 2.0,  "diameter": 0.05, "viscosity": 0.001},
    "oil":      {"density": 900,  "velocity": 0.5,  "diameter": 0.05, "viscosity": 0.1},
    "air":      {"density": 1.2,  "velocity": 15.0, "diameter": 0.1,  "viscosity": 0.000018},
    "glycerin": {"density": 1260, "velocity": 0.1,  "diameter": 0.05, "viscosity": 1.5}
}
# 1. Calculate Reynolds number for each fluid
for i in pipes:
    re = pipes[i]["density"]*pipes[i]["velocity"]*pipes[i]["diameter"]/pipes[i]["viscosity"]
    print(f"{i} Re is {re}")

2. #Print fluid name, Re value, and flow type:
#    Re < 2300         → Laminar
#    2300 to 4000      → Transitional
#    Above 4000        → Turbulent
for i in pipes:
    re = pipes[i]["density"]*pipes[i]["velocity"]*pipes[i]["diameter"]/pipes[i]["viscosity"]
    if re < 2300:
        flow = "Laminar"
    elif 2300 <= re <= 4000:
        flow = "Transitional"
    else:
        flow = "Turbulent"
    print(f"{i} - Re: {re:.2f} - {flow}")

# 3. Count how many are turbulent
turbulent = 0
for i in pipes:
    re = pipes[i]["density"]*pipes[i]["velocity"]*pipes[i]["diameter"]/pipes[i]["viscosity"]
    if re > 4000:
        flow = "Turbulent"
        turbulent = turbulent + 1
print(f"Total number of turbulent flow liquids are: {turbulent}")

# 4. Print which fluid has the highest Reynolds number
highest_re = 0
highest_re_fluids = " "
for i in pipes:
    re = pipes[i]["density"]*pipes[i]["velocity"]*pipes[i]["diameter"]/pipes[i]["viscosity"]
    if re > highest_re:
        highest_re = re
        highest_re_fluids = i
print(f"The highest re is: {highest_re_fluids} - {highest_re:.2f}")