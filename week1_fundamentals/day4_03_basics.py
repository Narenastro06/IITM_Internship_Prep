# Problem 27: You have 5 students and their marks
# names = ["Naren", "Raj", "Priya", "Kumar", "Divya"]
# marks = [85, 90, 45, 78, 60]

names = ["Naren", "Raj", "Priya", "Kumar", "Divya"]
marks = [85, 90, 45, 78, 60]

for i in range(len(names)):
    if marks[i]>=50:
        print(names[i], marks[i], "PASS")
    else:
        print(names[i], marks[i], "FAIL")
