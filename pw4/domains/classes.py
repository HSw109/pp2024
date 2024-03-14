class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.course_marks = {}

    def add_course_mark(self, course_id, mark):
        self.course_marks[course_id] = mark

    def __repr__(self):
        return f"ID: {self.student_id}, Name: {self.name}"

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.mark = None

    def set_mark(self, mark):
        self.mark = mark

    def __repr__(self):
        return f"ID: {self.course_id}, Name: {self.name}"

class SchoolSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    # Other methods can be added here
