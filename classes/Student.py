class Student:
    def __init__(self, occ_id, first_name, last_name, email, password):
        self.student_occ_id = occ_id
        self.student_first_name = first_name
        self.student_last_name = last_name
        self.student_email = email
        self.student_password = password
        self.student_scores = []  # A list to store scores as float
        self.current_courses = []  # A list to store courses as Course objects
    
    # Getters
    def get_student_occ_id(self):
        return self.student_occ_id

    def get_student_first_name(self):
        return self.student_first_name

    def get_student_last_name(self):
        return self.student_last_name

    def get_student_email(self):
        return self.student_email

    def get_student_password(self):
        return self.student_password

    # Setters
    def set_student_first_name(self, first_name):
        self.student_first_name = first_name

    def set_student_last_name(self, last_name):
        self.student_last_name = last_name

    def set_student_email(self, email):
        self.student_email = email

    def set_student_password(self, password):
        self.student_password = password

    # Methods
    def add_student_score(self, score):
        self.student_scores.append(score)

    def add_course(self, course):
        self.current_courses.append(course)

    def calculate_grade(self):
        if not self.student_scores:
            return 0.0  # No scores available
        return sum(self.student_scores) / len(self.student_scores)