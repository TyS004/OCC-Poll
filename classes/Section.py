class Section:
    def __init__(self, add_code, section_id = 000000):
        self.add_code = add_code
        self.section_id = section_id
        self.student_grades = {}

    def get_add_code(self):
        return self.add_code

    def get_section_id(self):
        return self.section_id

    def set_section_id(self, section_id):
        self.section_id = section_id

    def get_student_grades(self):
        return self.student_grades

    def add_student_grade(self, student_occ_id, student_score):
        self.student_grades[student_occ_id] = student_score