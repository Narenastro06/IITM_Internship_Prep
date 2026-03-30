#Problem 52: Write a function called calculate_strain
# It takes stress and E as inputs
# Formula: strain = stress / E
# Return the strain
# Call it with stress = 400e6 Pa, E = 200e9 Pa
# Print the result

def calculate_strain(stress, E):
    strain = stress/E
    return(strain)
result = calculate_strain(400e6, 200e9)
print(f"The strain is: {result}")