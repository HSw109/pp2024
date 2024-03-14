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
