stress_values = [120, 250, 180, 300, 95, 210, 175, 340, 160, 220]
highest = 0
lowest = 99999
total = 0
for i in range(len(stress_values)):
    if stress_values[i] > highest:
        highest = stress_values[i]
    if stress_values[i] < lowest:
        lowest = stress_values[i]
    total = total + stress_values[i]
print(f"The highest value is: {highest}")
print(f"The lowest value is: {lowest}")
print(f"Total is: {total}")