#Problem 50: Pressure builds up in a vessel
# pressure = 0 Pa
# Increases by 50000 Pa each loop
# Safety limit = 500000 Pa
# Stop when pressure exceeds safety limit
# Print pressure in MPa after each increase

pressure = 0 #in Pa
while pressure < 500000:
    print(f"The safety limit is: {pressure/1e6} MPa")
    pressure = pressure + 50000
