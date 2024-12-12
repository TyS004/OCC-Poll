import Section as s

class Course:
    def __init__(self, semester, sections, course_id = 000000):
        self.semester = semester
        self.course_id = course_id
        self.sections = sections

    def get_course_id(self):
        return self.course_id

    def get_semester(self):
        return self.semester

    def get_sections(self):
        return self.sections

    def set_course_id(self, course_id):
        self.course_id = course_id

    def set_semester(self, semester):
        self.semester = semester

