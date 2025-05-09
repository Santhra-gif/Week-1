# Python program (based on OOPS concept) for student management system with basic operations - add student, remove student , search and display

class Student:
    def __init__(self, name, rollno, student_class):
        self.name = name
        self.rollno = rollno
        self.student_class = student_class

    # To display student details
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.rollno}")
        print(f"Class: {self.student_class}")
        print("-" * 20)


class StudentManagement:
    def __init__(self):
        self.students = []  # list to store Student objects

    def add_student(self):
        name = input("Enter student's name: ")
        rollno = int(input("Enter roll number: "))
        student_class = input("Enter class: ")
        
        # Create a new student and add to list
        new_student = Student(name, rollno, student_class)
        self.students.append(new_student)
        print("Student added successfully!\n")
    
    # To display all students
    def display_all(self):
        if not self.students:
            print("No students in the system.\n")
        else:
            print("\nList of Students:\n")
            for student in self.students:
                student.display()
    
    # To search a student
    def search_student(self):
        rollno = int(input("Enter roll number to search: "))
        for student in self.students:
            if student.rollno == rollno:
                print("\nStudent Found:\n")
                student.display()
                return
        print("Student not found.\n")

    # To delete a student
    def delete_student(self):
        rollno = int(input("Enter roll number to delete: "))
        for i, student in enumerate(self.students):
            if student.rollno == rollno:
                del self.students[i]
                print("Student deleted successfully!\n")
                return
        print("Student not found.\n")


def main():
    sm = StudentManagement()

    while True:
        print("\n..................Student Management System......................")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            sm.add_student()
        elif choice == '2':
            sm.display_all()
        elif choice == '3':
            sm.search_student()
        elif choice == '4':
            sm.delete_student()
        elif choice == '5':
            print("Thank you for using Student Management System!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.\n")


if __name__ == "__main__":
    main()