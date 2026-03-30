# Problem 58: Write a function called pipe_flow
# Takes: pressure_diff, viscosity, radius, length
# Formula: flow_rate = (pi * radius^4 * pressure_diff) / (8 * viscosity * length)
# While radius increases by 0.005 each step
# Stop when flow_rate exceeds 0.01 m³/s
# Return final radius and flow_rate
# Call it: pipe_flow(1000, 0.001, 0.01, 1.0)
# Print: "Radius: X m - Flow Rate: X m³/s"
pi = 3.14
def pipe_flow(pressure_diff, viscosity, radius, length):
    flow_rate = (pi*(radius**4)*pressure_diff) / (8*viscosity*length)
    while flow_rate < 0.01: #in m³/s
         radius = radius + 0.005
         flow_rate = (pi*(radius**4)*pressure_diff) / (8*viscosity*length)
    return flow_rate, radius
flow_rate, radius = pipe_flow(1000, 0.001, 0.01, 1.0)
print(f"Radius {radius} m - Flow Rate {flow_rate} m³/s")