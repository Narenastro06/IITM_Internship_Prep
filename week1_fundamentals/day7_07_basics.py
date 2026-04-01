# Mini Challenge 4 — Fluid Mechanics
# Pressure drop in a pipe using Darcy-Weisbach equation
# Formula: dP = f * (L/D) * (density * velocity² / 2)
# f = friction factor (given)
# L = pipe length (m)
# D = pipe diameter (m)

#pipes = {
#    "water": {"density": 1000, "velocity": 2.0,  "diameter": 0.05, "length": 10, "friction": 0.02},
#    "oil": {"density": 900,  "velocity": 0.5,  "diameter": 0.05, "length": 10, "friction": 0.03},
#    "air": {"density": 1.2,  "velocity": 15.0, "diameter": 0.1,  "length": 10, "friction": 0.015},
#    "glycerin": {"density": 1260, "velocity": 0.1,  "diameter": 0.05, "length": 10, "friction": 0.04}
#}

# Tasks:
#1. Calculate pressure drop for each fluid and print fluid name and pressure drop in Pa
#2. Print which fluid has the highest pressure drop
#3. Print which fluid has the lowest pressure drop

pipes = {
    "water": {"density": 1000, "velocity": 2.0,  "diameter": 0.05, "length": 10, "friction": 0.02},
    "oil": {"density": 900,  "velocity": 0.5,  "diameter": 0.05, "length": 10, "friction": 0.03},
    "air": {"density": 1.2,  "velocity": 15.0, "diameter": 0.1,  "length": 10, "friction": 0.015},
    "glycerin": {"density": 1260, "velocity": 0.1,  "diameter": 0.05, "length": 10, "friction": 0.04}
}
highest = 0
highest_pressure_drop = ""
lowest = float('inf')
lowest_pressure_drop = ""
for i in pipes:
# 1. Calculate pressure drop for each fluid and print fluid name and pressure drop in Pa
    dP = pipes[i]["friction"] * (pipes[i]["length"]/pipes[i]["diameter"]) * (pipes[i]["density"] * pipes[i]["velocity"]**2 / 2)
    print(f"The Pressure drop in {i} is {dP} Pa")

#2. Print which fluid has the highest pressure drop
    if dP > highest:
        highest = dP
        highest_pressure_drop = i

#3. Print which fluid has the lowest pressure drop
    if dP < lowest:
        lowest = dP
        lowest_pressure_drop = i
print(f"{highest_pressure_drop} has highest pressure drop - {highest} Pa")
print(f"{lowest_pressure_drop} has lowest pressure drop - {lowest} Pa")
