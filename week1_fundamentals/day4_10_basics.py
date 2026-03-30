# Problem 34: You have a list of temperatures in Celsius
# temps = [0, 25, 37, 100, -10]
# Convert each to Fahrenheit and print
# Formula: F = (C × 9/5) + 32

temp = [0, 25, 37, 100, -10]
for i in range(len(temp)):
    F = (temp[i]*(9/5))+32
    print(f"The Fahrenheit temperatures are: {F}")