class Golfer:

    def __init__(self, name):

        self.name = name

        self.rounds = []

    def add_round(self, round_played):

        self.rounds.append(round_played)

    def get_round_count(self):

        return len(self.rounds)