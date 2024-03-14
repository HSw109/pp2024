from input import *
from domains.classes import Student, Course, SchoolSystem
import numpy as np

school_system = SchoolSystem()

def list_courses(self):
        print("List of Courses:")
        for course in self.courses.values():
            print(course)

def list_students(self):
    print("List of Students:")
    for student in self.students.values():
        print(student)

def print_course_mark(self):
    course_id = input("Enter course id: ")
    if course_id in self.courses and self.courses[course_id].mark is not None:
        print(f"Mark for {self.courses[course_id].name}: {self.courses[course_id].mark}")
    else:
        print("Course not found or mark not available")

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

while True:
    print("1. Input number of students")
    print("2. Input id, name, DoB of student")
    print("3. Input number of courses")
    print("4. Input id, name of course")
    print("5. Input marks for each student-course combination")
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
        num_students = input_students_number()
    elif option == 2:
        for _ in range(num_students):
            student_info = input_student_info()
            student = Student(**student_info)
            school_system.students[student_info["student_id"]] = student
    elif option == 3:
        num_courses = input_courses_number()
    elif option == 4:
        for _ in range(num_courses):
            course_info = input_course_info()
            course = Course(**course_info)
            school_system.courses[course_info["course_id"]] = course
    elif option == 5:
        input_student_course_marks(school_system.students, school_system.courses)
    elif option == 6:
        school_system.list_courses()
    elif option == 7:
        school_system.list_students()
    elif option == 8:
        school_system.print_course_mark()
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
    else:
        print("Invalid, please choose appropriate option")
