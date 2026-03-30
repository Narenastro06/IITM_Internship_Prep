#Problem 44: Water tank has 1000 litres
# Every loop, 50 litres drains out
# Stop when tank is empty
# Print volume after each drain

water_tank = 1000 #in litres
while water_tank > 0:
    print(f"Volume after each drain is: {water_tank}")
    water_tank = water_tank - 50