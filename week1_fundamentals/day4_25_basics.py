#Problem 48: A car is braking
# speed = 120 km/h
# Decreases by 15 each loop
# Stop when speed reaches 0
# Print each speed
# Also print: Safe if speed < 40, Caution if 40-80, Danger if above 80

speed = 120 #in km/h
while speed > 0:
    print(f"The speed is: {speed}")
    speed = speed - 15
    if speed == 0:
        print("The car has stopped.")
    elif speed < 40:
        print("Safe")
    elif speed >= 40 and speed <= 80:
        print("Caution")
    else:
        print("Danger")