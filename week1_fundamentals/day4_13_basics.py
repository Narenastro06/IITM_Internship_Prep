#Problem 37: numbers = [3, 6, 9, 12, 15]
# Print the sum of all numbers without using sum()

numbers = [3, 6, 9, 12, 15]
sum = 0
for i in range(len(numbers)):
    sum = numbers[i]+sum

print(f"sum of all numbers is: {sum}")