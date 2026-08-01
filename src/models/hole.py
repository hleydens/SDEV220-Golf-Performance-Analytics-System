"""
hole.py
Represents a single hole in a round of golf.
"""

from src.models.shot import Shot


class Hole:


    def __init__(self, hole_number: int, par: int):
        self.hole_number = hole_number
        self.par = par
        self.shots = []
        self.completed = False

    # ---------------------------------------------------------
    # Shot Management
    # ---------------------------------------------------------

    def add_shot(self, shot: Shot):
        """Adds a shot to the hole."""
        if self.completed:
            raise ValueError("Cannot add a shot to a completed hole.")

        self.shots.append(shot)

    def hole_out(self):
        """Marks the hole as complete."""
        self.completed = True

    # ---------------------------------------------------------
    # Statistics
    # ---------------------------------------------------------

    def get_score(self):
        """Returns the score for the hole."""
        return len(self.shots)

    def get_next_shot_number(self):
        return len(self.shots) + 1

    def get_putts(self):
        """Returns the number of putts."""
        return sum(
            1
            for shot in self.shots
            if shot.shot_type.lower() == "putt"
        )

    def get_penalties(self):
        """Returns the number of penalty shots."""
        return sum(
            1
            for shot in self.shots
            if shot.penalty
        )

    def is_complete(self):
        """Returns True if the hole has been completed."""
        return self.completed

    # ---------------------------------------------------------
    # JSON Serialization
    # ---------------------------------------------------------

    def to_dict(self):
        return {
            "hole_number": self.hole_number,
            "par": self.par,
            "completed": self.completed,
            "shots": [
                shot.to_dict()
                for shot in self.shots
            ]
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Hole from a dictionary."""
        hole = cls(
            hole_number=data["hole_number"],
            par=data["par"]
        )

        hole.completed = data.get("completed", False)

        hole.shots = [
            Shot.from_dict(shot)
            for shot in data.get("shots", [])
        ]

        return hole

    # ---------------------------------------------------------
    # String Representation
    # ---------------------------------------------------------

    def __str__(self):
        return (
            f"Hole {self.hole_number} "
            f"(Par {self.par}) - "
            f"Score: {self.get_score()}"
        )