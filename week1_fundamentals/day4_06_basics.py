# Problem 30: Find the LOWEST mark and who got it
# Same lists
# Output: "Priya got the lowest mark: 45"

names = ["Naren", "Raj", "Priya", "Kumar", "Divya"]
marks = [85, 90, 45, 78, 60]
lowest = marks[0]
top_name = ""
for i in range (len(names)):
    if marks[i] < lowest:
        lowest = marks[i]
        top_name = names[i]
print(top_name,"got the lowest mark: ", lowest)