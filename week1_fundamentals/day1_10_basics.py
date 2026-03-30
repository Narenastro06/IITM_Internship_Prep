#Problem 7: A rectangular steel beam has length = 3m, width = 0.2m, height = 0.3m. 
#Calculate its volume and mass (density of steel = 7850 kg/m³).

density = 7850 #Density of steel inkg/m³
l = 3 #Length of rectangle 
w = 0.2 #Width of rectangle 
h = 0.3 #Height of rectangle
V = l*w*h
print("The volume of the rectanglular steel beam is: ",V)
mass = density*V
print("The mass of rectangluar steel beam is: ", mass)