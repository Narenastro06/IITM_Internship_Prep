# Mini Challenge 2
# You are given this data:

#students = ["Naren", "Raj", "Priya", "Kumar", "Divya"]
#marks =    [85,      90,    45,      78,       60]

# Tasks:
# 1. Print each student's name, mark and grade (A/B/C/FAIL)
#    90 and above → A
#    75 to 89 → B
#    50 to 74 → C
#    Below 50 → FAIL
#
# 2. Count how many students passed (50 and above)
# 3. Count how many students failed
# 4. Print the topper (student with highest mark)
# 5. Print the class average

students = ["Naren", "Raj", "Priya", "Kumar", "Divya"]
marks = [85, 90, 45, 78, 60]

# 1. Print each student's name, mark and grade (A/B/C/FAIL)
#    90 and above → A
#    75 to 89 → B
#    50 to 74 → C
#    Below 50 → FAIL

for i in range(len(students)):
    if marks[i] >= 90:
        print(f"{students[i]} {marks[i]}, A")
    elif 75<= marks[i] <= 89:
        print(f"{students[i]} {marks[i]}, B")
    elif 50<= marks[i] <= 74:
        print(f"{students[i]} {marks[i]}, C")
    else:
        print(f"{students[i]} {marks[i]}, Fail")

# 2. Count how many students passed (50 and above)
students_passed = 0
for i in range(len(students)):
    if marks[i]>= 50: 
        students_passed = students_passed + 1
        
print(f"The number of students passed are: {students_passed}")

# 3. Count how many students failed
students_failed = 0
for i in range(len(students)):
    if marks[i]< 50: 
        students_failed = students_failed + 1

print(f"The number of students failed are: {students_failed}")

# 4. Print the topper (student with highest mark)
highest_mark = marks[0]
top_name = ""
for i in range(len(students)):
    if marks[i] > highest_mark:
        highest_mark = marks[i]
        top_name = students[i]

print(top_name,"got the highest mark: ", highest_mark)

# 5. Print the class average
total = 0
for i in range(len(students)):
    total = total+marks[i]

avg = total/len(marks)
print("Class average:", avg)