class Instructor:
    def __init__(self, instructor_occ_id, instructor_email, instructor_name):
        self.instructor_occ_id = instructor_occ_id 
        self.instructor_email = instructor_email  
        self.instructor_name = instructor_name 
        self.current_open_polls = []  
        self.current_courses = []  

    def get_instructor_occ_id(self):
        return self.instructor_occ_id

    def get_instructor_email(self):
        return self.instructor_email

    def get_instructor_name(self):
        return self.instructor_name

    def get_current_open_polls(self):
        return self.current_open_polls

    def add_poll_to_open_poll_list(self, poll):
        self.current_open_polls.append(poll)

    def create_course(self, course):
        self.current_courses.append(course)
