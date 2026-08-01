import tkinter as tk
from tkinter import Button, Frame, Label

from src.analytics import Analytics


class RoundAnalysisScreen(Frame):

    def __init__(self, app):
        super().__init__(app.root)

        self.app = app
        self.round_obj = app.selected_round
        print(self.round_obj)

        Label(
            self,
            text="Round Analysis",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        if self.round_obj is None:

            Label(
                self,
                text="No round selected."
            ).pack(pady=20)

            Button(
                self,
                text="Back",
                command=self.app.show_round_history
            ).pack(pady=10)

            return

        # -------------------------------------------------
        # Course Information
        # -------------------------------------------------

        info_frame = Frame(self)
        info_frame.pack(fill="x", padx=20, pady=5)

        Label(
            info_frame,
            text=f"Course: {self.round_obj.course.name}",
            anchor="w"
        ).pack(fill="x")

        Label(
            info_frame,
            text=f"Date: {self.round_obj.date}",
            anchor="w"
        ).pack(fill="x")

        # -------------------------------------------------
        # Overall
        # -------------------------------------------------

        overall = Frame(
            self,
            relief="groove",
            bd=2
        )

        overall.pack(fill="x", padx=20, pady=5)

        Label(
            overall,
            text="Overall",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        Label(
            overall,
            text=f"Score: {Analytics.score(self.round_obj)}"
        ).pack(anchor="w", padx=10)

        Label(
            overall,
            text=f"Score to Par: {Analytics.score_to_par(self.round_obj):+}"
        ).pack(anchor="w", padx=10)

        Label(
            overall,
            text=f"Putts: {Analytics.putts(self.round_obj)}"
        ).pack(anchor="w", padx=10)

        Label(
            overall,
            text=f"Penalty Strokes: {Analytics.penalties(self.round_obj)}"
        ).pack(anchor="w", padx=10)

        # -------------------------------------------------
        # Scoring
        # -------------------------------------------------

        scoring = Frame(
            self,
            relief="groove",
            bd=2
        )

        scoring.pack(fill="x", padx=20, pady=5)

        Label(
            scoring,
            text="Scoring",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        Label(
            scoring,
            text=f"Birdies: {Analytics.birdies(self.round_obj)}"
        ).pack(anchor="w", padx=10)

        Label(
            scoring,
            text=f"Pars: {Analytics.pars(self.round_obj)}"
        ).pack(anchor="w", padx=10)

        Label(
            scoring,
            text=f"Bogeys: {Analytics.bogeys(self.round_obj)}"
        ).pack(anchor="w", padx=10)

        Label(
            scoring,
            text=f"Double Bogeys: {Analytics.double_bogeys(self.round_obj)}"
        ).pack(anchor="w", padx=10)

        Label(
            scoring,
            text=f"Triple+ Bogeys: {Analytics.triple_plus(self.round_obj)}"
        ).pack(anchor="w", padx=10)

        # -------------------------------------------------
        # Hole Performance
        # -------------------------------------------------

        holes = Frame(
            self,
            relief="groove",
            bd=2
        )

        holes.pack(fill="x", padx=20, pady=5)

        Label(
            holes,
            text="Hole Performance",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        Label(
            holes,
            text=f"Average Par 3 Score: {Analytics.average_par3_score(self.round_obj):.2f}"
        ).pack(anchor="w", padx=10)

        Label(
            holes,
            text=f"Average Par 4 Score: {Analytics.average_par4_score(self.round_obj):.2f}"
        ).pack(anchor="w", padx=10)

        Label(
            holes,
            text=f"Average Par 5 Score: {Analytics.average_par5_score(self.round_obj):.2f}"
        ).pack(anchor="w", padx=10)

        # -------------------------------------------------
        # Navigation
        # -------------------------------------------------
        Button(
            self,
            text="View Hole Scores",
            width=20,
            command=self.app.show_hole_scores
        ).pack(pady=5)


        Button(
            self,
            text="Back",
            width=20,
            command=self.app.show_round_history
        ).pack(pady=15)

        hole_frame = Frame(
            self,
            relief="groove",
            bd=2
        )

        hole_frame.pack(fill="x", padx=20, pady=5)

        Label(
            hole_frame,
            text="Hole Scores",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        header = Frame(hole_frame)
        header.pack(fill="x", padx=10)

        Label(header, text="Hole", width=8, font=("Arial", 10, "bold")).grid(row=0, column=0)
        Label(header, text="Par", width=8, font=("Arial", 10, "bold")).grid(row=0, column=1)
        Label(header, text="Score", width=8, font=("Arial", 10, "bold")).grid(row=0, column=2)

        for hole in self.round_obj.holes:

            score = hole.get_score()
            difference = score - hole.par

            row = Frame(hole_frame)
            row.pack(fill="x", padx=10)

            Label(row, text=hole.hole_number, width=8).grid(row=0, column=0)
            Label(row, text=hole.par, width=8).grid(row=0, column=1)
            Label(row, text=score, width=8).grid(row=0, column=2)
            Label(row, text=f"{difference:+}", width=8).grid(row=0, column=3)
