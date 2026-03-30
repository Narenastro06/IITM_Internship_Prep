# Problem 35: You have a list of numbers
# numbers = [4, 7, 2, 9, 1, 5, 8, 3]
# Print only the even numbers

numbers = [4, 7, 2, 9, 1, 5, 8, 3]
for i in range(len(numbers)):
    if numbers[i] %2 == 0:
        print(numbers[i])