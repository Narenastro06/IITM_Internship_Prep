# WEEK 1 REVISION CHALLENGE
# You have 5 fluid samples in a dictionary
# Each has: viscosity, density, shear_rate
# 
# Write a function that:
# 1. Calculates shear stress = viscosity * shear_rate
# 2. Classifies: Low/Medium/High
# 3. Loop through all samples
# 4. Print each sample, shear stress, classification
# 5. Find highest shear stress sample
# 6. Print average shear stress
#
# Use: function, for loop, if/elif/else

samples = ["sample_1", "sample_2", "sample_3", "sample_4", "sample_5"]
viscosity = [0.001, 0.05, 0.5, 2.0, 0.0001]
shear_rate = [100, 50, 20, 10, 200]


for i in range(len(samples)):
    shear_stress = viscosity[i]*shear_rate[i]
    print(f"Shear rate of the sample is {samples[i]} - {shear_stress}")

def calc_shear(viscosity, shear_rate):
    shear_stress = viscosity*shear_rate
    if shear_stress < 1:
        classification = "LOW"
    elif 1 < shear_stress < 10:
        classification = "MEDIUM"
    else:
        classification = "HIGH"
    return shear_stress, classification

for i in range(len(samples)):
    shear_stress, classification = calc_shear(viscosity[i], shear_rate[i])
    print(f"{samples[i]} - Shear Stress: {shear_stress} - {classification}")

highest = 0
name = ""
total = 0
for i in range(len(samples)):
    shear_stress = viscosity[i]*shear_rate[i]
    if shear_stress > highest:
        highest = shear_stress
        name = samples[i]
    total = total + shear_stress
    avg = total/len(samples)

    
print(f"{name} has the highest shear stress: {highest}")
print(f"Average shear stress: {avg:.2f}")