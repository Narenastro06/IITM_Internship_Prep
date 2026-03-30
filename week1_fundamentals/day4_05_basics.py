# Problem 29: Find the highest mark and who got it
# names = ["Naren", "Raj", "Priya", "Kumar", "Divya"]
# marks = [85, 90, 45, 78, 60]
# Output: "Raj got the highest mark: 90"

names = ["Naren", "Raj", "Priya", "Kumar", "Divya"]
marks = [85, 90, 45, 78, 60]
highest = 0
top_name = ""
for i in range (len(names)):
    if marks[i] > highest:
        highest = marks[i]
        top_name = names[i]
print(top_name,"got the highest mark: ", highest)