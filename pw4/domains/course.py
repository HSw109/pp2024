class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.mark = None

    def set_mark(self, mark):
        self.mark = mark

    def __repr__(self):
        return f"ID: {self.course_id}, Name: {self.name}"
