

class Shot:
    """
    Represents a single golf shot.
    """

    def __init__(
        self,
        shot_number,
        club,
        shot_type,
        lie,
        starting_distance,
        penalty=False,
        notes=""
    ):
        self.shot_number = shot_number
        self.club = club
        self.shot_type = shot_type
        self.lie = lie
        self.starting_distance = starting_distance
        self.penalty = penalty
        self.notes = notes

    # -------------------------------------------------
    # Serialization
    # -------------------------------------------------

    def to_dict(self):
        """
        Converts the Shot object into a dictionary.
        """
        return {
            "shot_number": self.shot_number,
            "club": self.club,
            "shot_type": self.shot_type,
            "lie": self.lie,
            "starting_distance": self.starting_distance,
            "penalty": self.penalty,
            "notes": self.notes
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a Shot object from a dictionary.
        """
        return cls(
            shot_number=data["shot_number"],
            club=data["club"],
            shot_type=data["shot_type"],
            lie=data["lie"],
            starting_distance=data["starting_distance"],
            penalty=data.get("penalty", False),
            notes=data.get("notes", "")
        )

    # -------------------------------------------------
    # Display
    # -------------------------------------------------

    def __str__(self):
        return (
            f"Shot {self.shot_number} | "
            f"{self.club} | "
            f"{self.shot_type} | "
            f"{self.lie} | "
            f"{self.starting_distance} yds"
        )