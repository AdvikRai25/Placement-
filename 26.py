students = []
marks = []
percentage = []
for i in range(5):
    name = input("Enter name: ")
    students.append(name)
    print("enter marks for student ", name)
    mark_sum = 0
    for j in range(3):
        mark = int(input("Enter mark for subject: "))
        mark_sum += mark
        marks.append(mark)
    student_percentage = round(mark_sum/300*100)
    percentage.append(student_percentage)
print()
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("---Student Results---")
for i in range(5):
    print(i+1,". ", students[i], ": ", percentage[i],"%")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")