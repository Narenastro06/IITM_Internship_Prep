# Problem 31: Calculate the average mark
# Same lists
# Output: "Class average: 71.6"

names = ["Naren", "Raj", "Priya", "Kumar", "Divya"]
marks = [85, 90, 45, 78, 60]

total = 0
for i in range(len(names)):
    total = total+marks[i]

avg = total/len(marks)
print("Class average:", avg)