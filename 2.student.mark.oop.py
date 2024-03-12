class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

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
        if course_id in self.courses:
            mark = int(input("Enter course mark: "))
            self.courses[course_id].mark = mark
            print(f"You selected {self.courses[course_id].name} with mark {mark}")
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
        else:
            print("Course not found or mark not available")

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
        print("9. Exit")

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
            break
        else:
            print("Invalid, please choose appropriate option")


