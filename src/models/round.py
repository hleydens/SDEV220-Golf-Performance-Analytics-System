"""
round.py
Represents one round of golf.
"""

from datetime import date

from src.models.hole import Hole


class Round:

    def __init__(self, course):
        self.course = course
        self.date = date.today().isoformat()

        self.current_hole_index = 0
        self.completed = False

        TEST_HOLES = 2

        self.holes = [
            Hole(i + 1, course.hole_pars[i])
            for i in range(len(course.hole_pars))
        ]

    # -------------------------------------------------
    # Hole Navigation
    # -------------------------------------------------

    def get_current_hole(self):
        return self.holes[self.current_hole_index]

    def get_current_hole_number(self):
        return self.current_hole_index + 1

    def complete_current_hole(self):
        self.get_current_hole().hole_out()

        if self.current_hole_index < len(self.holes) - 1:
            self.current_hole_index += 1
            return True

        self.completed = True
        return False

    def is_complete(self):
        return self.completed

    # -------------------------------------------------
    # Round Statistics
    # -------------------------------------------------

    def get_total_score(self):
        return sum(
            hole.get_score()
            for hole in self.holes
        )

    def get_total_putts(self):
        return sum(
            hole.get_putts()
            for hole in self.holes
        )

    def get_total_penalties(self):
        return sum(
            hole.get_penalties()
            for hole in self.holes
        )

    def get_course_par(self):
        return sum(self.course.hole_pars)

    def get_score_to_par(self):
        return self.get_total_score() - self.get_course_par()

    # -------------------------------------------------
    # JSON
    # -------------------------------------------------

    def to_dict(self):
        return {
            "course": self.course.name,
            "date": self.date,
            "completed": self.completed,
            "current_hole_index": self.current_hole_index,
            "holes": [
                hole.to_dict()
                for hole in self.holes
            ]
        }

    @classmethod
    def from_dict(cls, data, course):

        round_obj = cls(course)

        round_obj.date = data["date"]
        round_obj.completed = data["completed"]
        round_obj.current_hole_index = data.get(
            "current_hole_index",
            0
        )

        round_obj.holes = [
            Hole.from_dict(hole)
            for hole in data["holes"]
        ]

        return round_obj

    def __str__(self):
        return (
            f"{self.date} | "
            f"{self.course.name} | "
            f"{self.get_total_score()}"
        )