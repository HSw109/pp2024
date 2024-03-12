import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.mark = None

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.mark = None

class SchoolSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def input_student_num(self):
        num = int(input("Enter number of students: "))
        while num <= 0:
            print("Invalid, please choose a number greater than 0")
            num = int(input("Enter number of students: "))
        return num

    def input_student_info(self):
        student_id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB: ")
        return Student(student_id, name, dob)

    def input_course_num(self):
        num = int(input("Enter number of courses: "))
        while num <= 0:
            print("Invalid, please choose a number greater than 0")
            num = int(input("Enter number of courses: "))
        return num

    def input_course_info(self):
        course_id = input("Enter course id: ")
        name = input("Enter course name: ")
        return Course(course_id, name)

    def select_course(self):
        course_id = input("Enter course id: ")
        student_id = input("Enter student id for input course: ")
        if course_id in self.courses:
            mark = np.floor(int(input("Enter course mark: ")))

            self.courses[course_id].mark = mark
            self.students[student_id].mark = mark
            print(f"You selected {self.courses[course_id].name} with mark {mark} for {self.students[student_id].name}")
        else:
            print("Course not found")

    def list_courses(self):
        print("List of Courses:")
        for course_id, course in self.courses.items():
            print(f"ID: {course_id}, Name: {course.name}")

    def list_students(self):
        print("List of Students:")
        for student_id, student in self.students.items():
            print(f"ID: {student_id}, Name: {student.name}")

    def print_course_mark(self):
        course_id = input("Enter course id: ")
        if course_id in self.courses and self.courses[course_id].mark is not None:
            print(f"Mark for {self.courses[course_id].name}: {self.courses[course_id].mark}")
            print("Student Marks:")
            for student_id, student in self.students.items():
                if student.mark is not None and student.mark == self.courses[course_id].mark:
                    print(f"ID: {student_id}, Name: {student.name}, Mark: {student.mark}")
        else:
            print("Course not found or mark not available")

    def calculate_average_gpa(self, student_id):
        if student_id in self.students:
            marks = [course.mark for course in self.students[student_id].mark]
            gpa = np.mean(marks)
            print(f"Average GPA for {self.students[student_id].name}: {gpa}")
        else:
            print("Student not found")

    def calculate_weighted_sum(self, student_id):
        if student_id in self.students:
            marks = [course.mark for course in self.students[student_id].mark]
            credits = [course.credits for course in self.students[student_id].mark]
            weighted_sum = np.sum(np.multiply(marks, credits))
            print(f"Weighted Sum of Credits and Marks for {self.students[student_id].name}: {weighted_sum}")
        else:
            print("Student not found")

    def sort_students_by_gpa(self):
        student_list = list(self.students.values())
        sorted_students = sorted(student_list, key=lambda x: np.mean([course.mark for course in x.mark]), reverse=True)
        print("Sorted Students by GPA (descending):")
        for student in sorted_students:
            print(f"ID: {student.student_id}, Name: {student.name}, GPA: {np.mean([course.mark for course in student.mark])}")

# Main
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
            num_students = school_system.input_student_num()
        elif option == 2:
            for _ in range(num_students):
                student = school_system.input_student_info()
                school_system.students[student.student_id] = student
        elif option == 3:
            num_courses = school_system.input_course_num()
        elif option == 4:
            for _ in range(num_courses):
                course = school_system.input_course_info()
                school_system.courses[course.course_id] = course
        elif option == 5:
            school_system.select_course()
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
