import tkinter as tk

from src.screens.base_screen import BaseScreen
from src.analytics import Analytics


class StatisticsScreen(BaseScreen):

    def __init__(self, app):
        super().__init__(app)

        rounds = self.app.storage.get_rounds()

        tk.Label(
            self,
            text="Golf Statistics",
            font=("Arial", 20, "bold")
        ).pack(pady=15)

        self.stats_frame = tk.Frame(self)
        self.stats_frame.pack()

        self.display_statistics(rounds)

        tk.Button(
            self,
            text="Refresh Statistics",
            width=20,
            command=self.refresh
        ).pack(pady=15)

        tk.Button(
            self,
            text="Main Menu",
            width=20,
            command=self.app.show_welcome
        ).pack()

    # -------------------------------------------------

    def display_statistics(self, rounds):

        stats = [

            ("Rounds Played",
             Analytics.total_rounds(rounds)),

            ("Average Score",
             round(Analytics.average_score(rounds), 1)),

            ("Best Score",
             Analytics.best_score(rounds)),

            ("Worst Score",
             Analytics.worst_score(rounds)),

            ("Average To Par",
             round(Analytics.average_score_to_par(rounds), 1)),

            ("Average Putts",
             round(Analytics.average_putts(rounds), 1)),

            ("Average Penalty Strokes",
             round(Analytics.average_penalties(rounds), 1))

        ]

        for label, value in stats:

            tk.Label(
                self.stats_frame,
                text=f"{label}: {value}",
                anchor="w",
                width=30,
                font=("Arial", 12)
            ).pack(anchor="w", pady=2)

    # -------------------------------------------------

    def refresh(self):

        for widget in self.stats_frame.winfo_children():
            widget.destroy()

        rounds = self.app.storage.get_rounds()

        self.display_statistics(rounds)