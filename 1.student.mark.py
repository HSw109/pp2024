def inputStudentNum():
    num = int(input("Enter number of students: "))
    while num <= 0:
        print("Invalid, please choose a number greater than 0")
        num = int(input("Enter number of students: "))
    return num

def inputStudentInfo():
    student = {}
    student["id"] = input("Enter student id: ")
    student["name"] = input("Enter student name: ")
    student["DoB"] = input("Enter student DoB: ")
    return student

def inputCourseNum():
    num = int(input("Enter number of courses: "))
    while num <= 0:
        print("Invalid, please choose a number greater than 0")
        num = int(input("Enter number of courses: "))
    return num

def inputCourseInfo():
    course = {}
    course["id"] = input("Enter course id: ")
    course["name"] = input("Enter course name: ")
    return course

def selectCourse(courses):
    selected_course_id = input("Enter course id: ")
    if selected_course_id in courses:
        mark = int(input("Enter course mark: "))
        courses[selected_course_id]["mark"] = mark
        print(f"You selected {courses[selected_course_id]['name']} with mark {mark}")
    else:
        print("Course not found")

def listCourses(courses):
    print("List of Courses:")
    for course_id, course in courses.items():
        print(f"ID: {course_id}, Name: {course['name']}")

def listStudents(students):
    print("List of Students:")
    for student_id, student in students.items():
        print(f"ID: {student_id}, Name: {student['name']}")

def printCourseMark(courses):
    course_id = input("Enter course id: ")
    if course_id in courses and "mark" in courses[course_id]:
        print(f"Mark for {courses[course_id]['name']}: {courses[course_id]['mark']}")
    else:
        print("Course not found or mark not available")

# Main
students = {}
courses = {}

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
        num_students = inputStudentNum()
    elif option == 2:
        for _ in range(num_students):
            student_info = inputStudentInfo()
            students[student_info["id"]] = student_info
    elif option == 3:
        num_courses = inputCourseNum()
    elif option == 4:
        for _ in range(num_courses):
            course_info = inputCourseInfo()
            courses[course_info["id"]] = course_info
    elif option == 5:
        selectCourse(courses)
    elif option == 6:
        listCourses(courses)
    elif option == 7:
        listStudents(students)
    elif option == 8:
        printCourseMark(courses)
    elif option == 9:
        break
    else:
        print("Invalid, please choose appropriate option")


