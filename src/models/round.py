from src.models.hole import Hole


class Round:

    def __init__(self, course):

        self.course = course
        self.current_hole = 1
        self.holes = []

        for hole_number, par in enumerate(course.hole_pars, start=1):
            self.holes.append(Hole(hole_number, par))

    def get_current_hole(self):

        return self.holes[self.current_hole - 1]

    def next_hole(self):

        if self.current_hole < 18:
            self.current_hole += 1
            return True

        return False

    def is_finished(self):

        return self.current_hole == 18

    def get_total_score(self):

        return sum(hole.get_score() for hole in self.holes)