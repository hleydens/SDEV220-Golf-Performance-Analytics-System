from src.models.shot import Shot


class Hole:

    def __init__(self, hole_number, par):

        self.hole_number = hole_number
        self.par = par
        self.shots = []

    def add_shot(
        self,
        club,
        shot_type,
        lie,
        starting_distance,
        good_shot
    ):

        shot = Shot(
            shot_number=len(self.shots) + 1,
            club=club,
            shot_type=shot_type,
            lie=lie,
            starting_distance=starting_distance,
            good_shot=good_shot
        )

        self.shots.append(shot)

        return shot

    def get_score(self):

        return len(self.shots)

    def get_putts(self):

        return sum(
            1
            for shot in self.shots
            if shot.shot_type == "Putt"
        )

    def __str__(self):

        return f"Hole {self.hole_number}"