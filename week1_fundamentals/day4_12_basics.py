#Problem 36: You have a list of prices
# prices = [120, 450, 89, 300, 675]
# Apply 10% discount to each and print the new price
prices = [120, 450, 89, 300, 675]
for i in range(len(prices)):
    discount = prices[i]*0.9
    print(f"The discount money is: {discount}")