# Problem 28: You have 5 students and their marks
# names = ["Naren", "Raj", "Priya", "Kumar", "Divya"]
# marks = [85, 90, 45, 78, 60]
# Print name, mark, and grade:
# 90 and above → A
# 75 to 89 → B
# 50 to 74 → C
# Below 50 → FAIL

names = ["Naren", "Raj", "Priya", "Kumar", "Divya"]
marks = [85, 90, 45, 78, 60]

for i in range(len(names)):
    if marks[i]>=90:
        print(names[i], marks[i], "A")
    elif 75<= marks[i] <=89: 
        print(names[i], marks[i], "B")
    elif 50<= marks[i] <=74: 
        print(names[i], marks[i], "C")
    else:
        print(names[i], marks[i], "FAIL")

