from input import SchoolSystemInput
from domains.student import Student
from domains.course import Course
import numpy as np

class SchoolSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def list_courses(self):
        print("List of Courses:")
        for course in self.courses.values():
            print(course)

    def list_students(self):
        print("List of Students:")
        for student in self.students.values():
            print(student)

    def calculate_average_gpa(self, student_id):
        if student_id in self.students:
            marks = list(self.students[student_id].course_marks.values())
            gpa = np.mean(marks)
            print(f"Average GPA for {self.students[student_id].name}: {gpa:.1f}")
        else:
            print("Student not found")

    def calculate_weighted_sum(self, student_id):
        if student_id in self.students:
            marks = list(self.students[student_id].course_marks.values())
            credits = [3, 4, 3]  # Example credits, replace with actual credits
            weighted_sum = np.dot(marks, credits)
            print(f"Weighted Sum of Credits and Marks for {self.students[student_id].name}: {weighted_sum}")
        else:
            print("Student not found")

    def sort_students_by_gpa(self):
        student_list = list(self.students.values())
        sorted_students = sorted(student_list, key=lambda x: np.mean(list(x.course_marks.values())), reverse=True)
        print("Sorted Students by GPA (descending):")
        for student in sorted_students:
            print(f"ID: {student.student_id}, Name: {student.name}, GPA: {np.mean(list(student.course_marks.values())):.1f}")


if __name__ == "__main__":
    school_system = SchoolSystem()
    while True:
        print("1. Input number of students")
        print("2. Input id, name, DoB of student")
        print("3. Input number of courses")
        print("4. Input id, name of course")
        print("5. Select course, input mark")
        print("6. List courses")
        print("7. List students")
        print("8. Show student mark for given course")
        print("9. Calculate average GPA for a student")
        print("10. Calculate weighted sum of credits and marks for a student")
        print("11. Sort students by GPA")
        print("12. Exit")

        option = input("Type a number option: ")

        try:
            option = int(option)
        except ValueError:
            print("Invalid, please choose appropriate option")
            continue

        if option == 1:
            num_students = SchoolSystemInput.input_students_number()
        elif option == 2:
            for _ in range(num_students):
                student_id, name, dob = SchoolSystemInput.input_student_info()
                school_system.students[student_id] = Student(student_id, name, dob)
        elif option == 3:
            num_courses = SchoolSystemInput.input_courses_number()
        elif option == 4:
            for _ in range(num_courses):
                course_id, name = SchoolSystemInput.input_course_info()
                school_system.courses[course_id] = Course(course_id, name)
        elif option == 5:
            SchoolSystemInput.select_course_and_input_mark(school_system.courses)
        elif option == 6:
            school_system.list_courses()
        elif option == 7:
            school_system.list_students()
        elif option == 8:
            SchoolSystemInput.print_course_mark(school_system.courses)
        elif option == 9:
            student_id = input("Enter student id: ")
            school_system.calculate_average_gpa(student_id)
        elif option == 10:
            student_id = input("Enter student id: ")
            school_system.calculate_weighted_sum(student_id)
        elif option == 11:
            school_system.sort_students_by_gpa()
        elif option == 12:
            break
