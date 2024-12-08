class Response:
    def __init__(self, content, points_awarded, timestamp):
        self.response_content = content
        self.points_awarded = points_awarded
        self.response_timestamp = timestamp

    def get_response_content(self):
        return self.response_content

    def get_points_awarded(self):
        return self.points_awarded

    def get_response_timestamp(self):
        return self.response_timestamp

    # Setters
    def set_response_content(self, content):
        self.response_content = content

    def set_points_awarded(self, points):
        self.points_awarded = points

    def set_response_timestamp(self, timestamp):
        self.response_timestamp = timestamp