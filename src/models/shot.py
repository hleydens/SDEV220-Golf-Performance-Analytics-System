from dataclasses import dataclass


@dataclass
class Shot:
    shot_number: int
    club: str
    shot_type: str
    lie: str
    starting_distance: int
    good_shot: bool

    def __str__(self):
        return (
            f"Shot {self.shot_number}: "
            f"{self.club} | "
            f"{self.shot_type} | "
            f"{self.lie} | "
            f"{self.starting_distance} yds"
        )