# Problem 32: Count how many students passed
# Pass mark is 50
# names = ["Naren", "Raj", "Priya", "Kumar", "Divya"]
# marks = [85, 90, 45, 78, 60]
# Output: "4 students passed"

names = ["Naren", "Raj", "Priya", "Kumar", "Divya"]
marks = [85, 90, 45, 78, 60]
passed_students = 0
for i in range(len(names)):
    if marks[i] >= 50:
        passed_students= passed_students + 1
print(f"{passed_students} passed the exam")