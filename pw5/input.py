import math

class SchoolSystemInput:
    @staticmethod
    def input_students_number():
        num = int(input("Enter number of students: "))
        while num <= 0:
            print("Invalid, please choose a number greater than 0")
            num = int(input("Enter number of students: "))
        return num

    @staticmethod
    def input_student_info():
        student_id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB: ")
        return student_id, name, dob

    @staticmethod
    def input_courses_number():
        num = int(input("Enter number of courses: "))
        while num <= 0:
            print("Invalid, please choose a number greater than 0")
            num = int(input("Enter number of courses: "))
        return num

    @staticmethod
    def input_course_info():
        course_id = input("Enter course id: ")
        name = input("Enter course name: ")
        return course_id, name

    @staticmethod
    def select_course_and_input_mark(students, courses):
        student_id = input("Enter student id: ")
        course_id = input("Enter course id: ")

        if student_id in students and course_id in courses:
            mark = float(input(f"Enter mark for {students[student_id].name} in {courses[course_id].name}: "))
            mark_rounded = math.floor(mark * 10) / 10  # Round down to 1 decimal place
            students[student_id].add_course_mark(course_id, mark_rounded)
            print(f"Mark {mark_rounded} added for {students[student_id].name} in {courses[course_id].name}")
        else:
            print("Student or course not found")

    @staticmethod
    def print_course_mark(courses):
        course_id = input("Enter course id: ")
        if course_id in courses and courses[course_id].mark is not None:
            print(f"Mark for {courses[course_id].name}: {courses[course_id].mark}")
        else:
            print("Course not found or mark not available")
