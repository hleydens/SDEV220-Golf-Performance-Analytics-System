"""
analytics.py
Calculates golf statistics from stored rounds.
"""


class Analytics:

    # -------------------------------------------------
    # Overall Statistics
    # -------------------------------------------------

    @staticmethod
    def total_rounds(rounds):
        return len(rounds)

    @staticmethod
    def average_score(rounds):

        if not rounds:
            return 0

        total = sum(
            round_obj.get_total_score()
            for round_obj in rounds
        )

        return round(total / len(rounds), 1)

    @staticmethod
    def best_score(rounds):

        if not rounds:
            return 0

        return min(
            round_obj.get_total_score()
            for round_obj in rounds
        )

    @staticmethod
    def worst_score(rounds):

        if not rounds:
            return 0

        return max(
            round_obj.get_total_score()
            for round_obj in rounds
        )

    @staticmethod
    def average_score_to_par(rounds):

        if not rounds:
            return 0

        total = sum(
            round_obj.get_score_to_par()
            for round_obj in rounds
        )

        return round(total / len(rounds), 1)

    # -------------------------------------------------
    # Per Hole Statistics
    # -------------------------------------------------

    @staticmethod
    def average_putts(rounds):

        if not rounds:
            return 0

        total_putts = 0
        total_holes = 0

        for round_obj in rounds:
            total_putts += round_obj.get_total_putts()
            total_holes += len(round_obj.holes)

        if total_holes == 0:
            return 0

        return round(total_putts / total_holes, 2)

    @staticmethod
    def average_penalties(rounds):

        if not rounds:
            return 0

        total = sum(
            round_obj.get_total_penalties()
            for round_obj in rounds
        )

        return round(total / len(rounds), 2)

    # -------------------------------------------------
    # Round Analysis
    # -------------------------------------------------

    @staticmethod
    def score(round_obj):
        return round_obj.get_total_score()

    @staticmethod
    def score_to_par(round_obj):
        return round_obj.get_score_to_par()

    @staticmethod
    def putts(round_obj):
        return round_obj.get_total_putts()

    @staticmethod
    def penalties(round_obj):
        return round_obj.get_total_penalties()

    @staticmethod
    def birdies(round_obj):

        total = 0

        for hole in round_obj.holes:

            difference = hole.get_score() - hole.par

            if difference == -1:
                total += 1

        return total


    @staticmethod
    def pars(round_obj):

        total = 0

        for hole in round_obj.holes:

            difference = hole.get_score() - hole.par

            if difference == 0:
                total += 1

        return total


    @staticmethod
    def bogeys(round_obj):

        total = 0

        for hole in round_obj.holes:

            difference = hole.get_score() - hole.par

            if difference == 1:
                total += 1

        return total


    @staticmethod
    def double_bogeys(round_obj):

        total = 0

        for hole in round_obj.holes:

            difference = hole.get_score() - hole.par

            if difference == 2:
                total += 1

        return total


    @staticmethod
    def triple_plus(round_obj):

        total = 0

        for hole in round_obj.holes:

            difference = hole.get_score() - hole.par

            if difference >= 3:
                total += 1

        return total

    @staticmethod
    def average_par3_score(round_obj):

        total_score = 0
        total_par3s = 0

        for hole in round_obj.holes:

            if hole.par == 3:

                total_score += hole.get_score()
                total_par3s += 1

        if total_par3s == 0:
            return 0

        return round(total_score / total_par3s, 2)

    @staticmethod
    def average_par4_score(round_obj):

        total_score = 0
        total_par4s = 0

        for hole in round_obj.holes:

            if hole.par == 4:

                total_score += hole.get_score()
                total_par4s += 1

        if total_par4s == 0:
            return 0

        return round(total_score / total_par4s, 2)


    @staticmethod
    def average_par5_score(round_obj):

        total_score = 0
        total_par5s = 0

        for hole in round_obj.holes:

            if hole.par == 5:

                total_score += hole.get_score()
                total_par5s += 1

        if total_par5s == 0:
            return 0

        return round(total_score / total_par5s, 2)