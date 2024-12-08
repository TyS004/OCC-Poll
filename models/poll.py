class Poll:
    def __init__(self, poll_id, question_type, correct_answers, points_worth, answers_to_select_from = None):
        self.poll_id = poll_id
        self.question_type = question_type
        self.correct_answers = correct_answers
        self.points_worth = points_worth
        self.answers_to_select_from = answers_to_select_from if answers_to_select_from else []
        self.poll_running = False

    def get_poll_id(self):
        return self.poll_id

    def set_poll_id(self, poll_id):
        self.poll_id = poll_id

    def get_question_type(self):
        return self.question_type

    def set_question_type(self, question_type):
        self.question_type = question_type

    def get_correct_answers(self):
        return self.correct_answers

    def set_correct_answers(self, correct_answers):
        self.correct_answers = correct_answers

    def get_points_worth(self):
        return self.points_worth

    def set_points_worth(self, points_worth):
        self.points_worth = points_worth

    def get_answers_to_select_from(self):
        return self.answers_to_select_from

    def set_answers_to_select_from(self, answers_to_select_from):
        self.answers_to_select_from = answers_to_select_from

    def open_poll(self):
        self.poll_running = True

    def close_poll(self):
        self.poll_running = False

    def is_running(self):
        return self.poll_running
