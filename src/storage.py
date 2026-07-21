class StorageManager:

    def __init__(self):

        self.golfers = []

        self.courses = []

    def add_golfer(self,golfer):

        self.golfers.append(golfer)

    def add_course(self,course):

        self.courses.append(course)

    def get_golfers(self):

        return self.golfers

    def get_courses(self):

        return self.courses