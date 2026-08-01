class Golfer:

    def __init__(self, name):
        self.name = name
        self.rounds = []

    def add_round(self, round_played):
        self.rounds.append(round_played)

    def get_round_count(self):
        return len(self.rounds)

    def get_average_score(self):
        if not self.rounds:
            return 0

        return sum(r.get_total_score() for r in self.rounds) / len(self.rounds)

    def get_best_round(self):
        if not self.rounds:
            return None

        return min(self.rounds, key=lambda r: r.get_total_score())

    def to_dict(self):
        return {
            "name": self.name,
            "rounds": [r.to_dict() for r in self.rounds]
        }

    @classmethod
    def from_dict(cls, data):
        golfer = cls(data["name"])
        return golfer