"""
storage.py
Handles loading and saving application data.
"""

import json
from pathlib import Path

from src.models.course import Course
from src.models.round import Round


class StorageManager:

    def __init__(self):

        self.data_folder = Path(__file__).parent / "data"

        self.course_file = self.data_folder / "courses.json"
        self.round_file = self.data_folder / "rounds.json"

        self.courses = []
        self.rounds = []

        self.load_data()

    # -------------------------------------------------
    # Master Load / Save
    # -------------------------------------------------

    def load_data(self):
        self.load_courses()
        self.load_rounds()

    def save_data(self):
        self.save_courses()
        self.save_rounds()

    # -------------------------------------------------
    # Courses
    # -------------------------------------------------

    def load_courses(self):

        if not self.course_file.exists():
            self.save_courses()
            return

        with open(self.course_file, "r") as file:
            data = json.load(file)

        self.courses = [
            Course.from_dict(course)
            for course in data
        ]

    def save_courses(self):

        with open(self.course_file, "w") as file:

            json.dump(
                [
                    course.to_dict()
                    for course in self.courses
                ],
                file,
                indent=4
            )

    # -------------------------------------------------
    # Rounds
    # -------------------------------------------------

    def load_rounds(self):

        if not self.round_file.exists():
            self.save_rounds()
            return

        with open(self.round_file, "r") as file:
            data = json.load(file)

        self.rounds = []

        for round_data in data:

            course = self.find_course(round_data["course"])

            if course is not None:
                self.rounds.append(
                    Round.from_dict(
                        round_data,
                        course
                    )
                )

    def save_rounds(self):

        with open(self.round_file, "w") as file:

            json.dump(
                [
                    round_obj.to_dict()
                    for round_obj in self.rounds
                ],
                file,
                indent=4
            )

    # -------------------------------------------------
    # Utility
    # -------------------------------------------------

    def find_course(self, course_name):

        for course in self.courses:

            if course.name == course_name:
                return course

        return None

    # -------------------------------------------------
    # Public Methods
    # -------------------------------------------------

    def add_course(self, course):

        self.courses.append(course)

        self.save_courses()

    def add_round(self, round_obj):

        self.rounds.append(round_obj)

        self.save_rounds()

    def get_courses(self):
        return self.courses

    def get_rounds(self):
        return self.rounds