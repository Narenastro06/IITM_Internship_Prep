#Problem 49: A rotating shaft slows down due to friction
# rpm = 3000
# Decreases by 200 rpm each loop
# Stop when rpm reaches 0
# Print each rpm value
# Also print: Overspeed if rpm > 2000, Normal if 1000-2000, Slow if below 1000

rpm = 3000
while rpm > 0:
    print(f"The rpm is: {rpm}")
    rpm = rpm - 200
    if rpm == 0:
        print("The shaft stops")
    elif rpm > 2000:
        print("Overspeed")
    elif rpm >=2000 and rpm <= 1000:
        print("Normal")
    else:
        print("Slow")