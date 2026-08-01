import tkinter as tk

from src.screens.base_screen import BaseScreen


class RoundSummaryScreen(BaseScreen):

    def __init__(self, app):
        super().__init__(app)

        round_obj = self.app.current_round

        if round_obj not in self.app.storage.get_rounds():
            self.app.storage.add_round(round_obj)

        tk.Label(
            self,
            text="Round Complete",
            font=("Arial", 20, "bold")
        ).pack(pady=10)

        tk.Label(
            self,
            text=f"Course: {round_obj.course.name}"
        ).pack()

        tk.Label(
            self,
            text=f"Date: {round_obj.date}"
        ).pack(pady=(0, 15))

        tk.Label(
            self,
            text=f"Score: {round_obj.get_total_score()}",
            font=("Arial", 14)
        ).pack()

        tk.Label(
            self,
            text=f"To Par: {round_obj.get_score_to_par()}",
            font=("Arial", 14)
        ).pack()

        tk.Label(
            self,
            text=f"Putts: {round_obj.get_total_putts()}",
            font=("Arial", 14)
        ).pack()

        tk.Label(
            self,
            text=f"Penalty Strokes: {round_obj.get_total_penalties()}",
            font=("Arial", 14)
        ).pack(pady=(0, 20))

        tk.Button(
            self,
            text="View Statistics",
            width=20,
            command=self.app.show_statistics
        ).pack(pady=5)

        tk.Button(
            self,
            text="Main Menu",
            width=20,
            command=self.app.show_welcome
        ).pack()