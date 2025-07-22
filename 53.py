class student:
    def _init_(self, name, marks):
        self.name = name
        self.marks = marks
        self.total_marks = sum(marks.values())
        self.percentage = self.total_marks / 4
        self.rank = 0

    def display(self):
        print("--- Student Details ---")
        print("Name: {}".format(self.name))
        print("Marks in 4 subjects: {}".format(self.marks))
        print("Percentage: {}%".format(self.percentage))
        print("Rank: {}".format(self.rank))
        print("-----------------------")


class college:
    def _init_(self):
        self.students = []

    def _update_ranks(self):
        self.students.sort(key=lambda s: s.percentage, reverse=True)
        index = 1
        for s in self.students:
            s.rank = index
            index += 1

    def add_new_student(self):
        name = input("Enter student name: ")
        marks = {
            "Physics": 0,
            "Chemistry": 0,
            "Maths": 0,
            "English": 0
        }
        for key, value in marks.items():
            marks[key] = int(input("Enter marks for subject {}: ".format(key)))
        s = student(name, marks)
        self.students.append(s)
        self._update_ranks()
        print("Student '{}' added successfully!".format(name))

    def view_topper(self):
        print("--- Topper ---")
        if not self.students:
            print("No students in the system yet.")
        else:
            topper = self.students[0]
            print("Topper is: {} with {}%".format(topper.name, topper.percentage))

    def view_individual_student_status(self):
        print("--- Individual student Status ---")
        if not self.students:
            print("No students in the system yet.")
            return

        name = input("Enter student name to view status: ")
        student_found = None
        for s in self.students:
            if s.name.lower() == name.lower():
                student_found = s
                break

        if student_found:
            student_found.display()
        else:
            print("Student with name '{}' not found.".format(name))

    def status_menu(self):
        while True:
            print("--- Status Menu ---")
            print("1. View Topper")
            print("2. Individual student Status")
            print("3. Back to Main Menu")

            choice = input("Enter choice: ")

            if choice == '1':
                self.view_topper()
            elif choice == '2':
                self.view_individual_student_status()
            elif choice == '3':
                break
            else:
                print("Invalid choice, please try again.")


c = college()

while True:
    print("===== Main Menu =====")
    print("1. Add New student")
    print("2. View Status")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        c.add_new_student()
    elif choice == '2':
        c.status_menu()
    elif choice == '3':
        print("Thank you for using our system...")
        break
    else:
        print("Invalid choice... please try again...")

'''class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.percentage = self.calculate_percentage()

    def calculate_percentage(self):
        total = sum(self.marks.values())
        return round((total / (len(self.marks) * 100)) * 100, 2)


class StudentManager:
    def __init__(self):
        self.student_list = []

    def add_student(self, name, marks):
        student = Students(name, marks)
        self.student_list.append(student)

    def find_topper(self):
        if not self.student_list:
            print("No students added yet.")
            return
        topper = max(self.student_list, key=lambda x: x.percentage)
        print(f"Topper is {topper.name} with {topper.percentage}%")

    def individual_status(self):
        if not self.student_list:
            print("No students added yet.")
            return
        name = input("Enter student name to view status: ")
        sorted_list = sorted(self.student_list, key=lambda x: x.percentage, reverse=True)
        found = False
       
        idx=1
        for student in sorted_list:
            if student.name == name:
                print(f"Name: {student.name}")
                print(f"Marks: {student.marks}")
                print(f"Percentage: {student.percentage}%")
                print(f"Rank: {idx}")
                idx=idx+1
                found = True
                break
        if not found:
            print("Student not found")


manager = StudentManager()

while True:
    print("MAIN MENU")
    print("1. Add new student")
    print("2. View status")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        os = int(input("Enter OS marks out of 100: "))
        ca = int(input("Enter CA marks out of 100: "))
        ds = int(input("Enter DS marks out of 100: "))
        marks = {"OS": os, "CA": ca, "DS": ds}
        manager.add_student(name, marks)
        print("Student added successfully")
   

    elif choice == '2':
        while True:
            print("STATUS MENU")
            print("1. View Topper")
            print("2. Individual Student Status")
            print("3. Back to Main Menu")
            sub_choice = input("Enter your choice: ")

            if sub_choice == '1':
                manager.find_topper()
            elif sub_choice == '2':
                manager.individual_status()
            elif sub_choice == '3':
                break
            else:
                print("Invalid choice. Try again.")

    elif choice == '3':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again")'''