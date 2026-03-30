#Problem 46: A fluid is heating up
# temp = 20 degrees C
# Increases by 5 degrees each loop
# Stop when temp exceeds 100 degrees
# Print each temperature

temp = 20 #in degrees C
while temp <= 100:
    print(f"The temperatures are: {temp} degrees C")
    temp = temp + 5
    