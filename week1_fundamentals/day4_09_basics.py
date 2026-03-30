# Problem 33: Print names of only the students who failed
# Pass mark is 50
# names = ["Naren", "Raj", "Priya", "Kumar", "Divya"]
# marks = [85, 90, 45, 78, 60]
# Output:
# Students who failed: Priya 45

names = ["Naren", "Raj", "Priya", "Kumar", "Divya"]
marks = [85, 90, 45, 78, 60]
for i in range(len(names)):
    if marks[i]< 50:
        print(names[i], marks[i])