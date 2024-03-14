def input_students_number():
    num = int(input("Enter number of students: "))
    while num <= 0:
        print("Invalid, please choose a number greater than 0")
        num = int(input("Enter number of students: "))
    return num

def input_student_info():
    student_id = input("Enter student id: ")
    name = input("Enter student name: ")
    dob = input("Enter student DoB: ")
    return {"student_id": student_id, "name": name, "dob": dob}

def input_courses_number():
    num = int(input("Enter number of courses: "))
    while num <= 0:
        print("Invalid, please choose a number greater than 0")
        num = int(input("Enter number of courses: "))
    return num

def input_course_info():
    course_id = input("Enter course id: ")
    name = input("Enter course name: ")
    return {"course_id": course_id, "name": name}

def input_student_course_marks(students, courses):
    for student_id, student in students.items():
        print(f"Input marks for courses for student ID: {student_id}, Name: {student.name}")
        for course_id, course in courses.items():
            mark = float(input(f"Enter mark for {course.name}: "))
            student.add_course_mark(course_id, mark)
