import tkinter as tk

from src.screens.base_screen import BaseScreen
from src.models.round import Round


class StartRoundScreen(BaseScreen):

    def __init__(self, app):
        super().__init__(app)

        self.course = self.app.storage.get_courses()[0]

        tk.Label(
            self,
            text="Start Round",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        tk.Label(
            self,
            text=self.course.name,
            font=("Arial", 16)
        ).pack(pady=10)

        tk.Label(
            self,
            text=f"Rating: {self.course.rating}"
        ).pack()

        tk.Label(
            self,
            text=f"Slope: {self.course.slope}"
        ).pack()

        tk.Label(
            self,
            text=f"Par: {self.course.par}"
        ).pack(pady=(0, 20))

        tk.Button(
            self,
            text="Start Round",
            command=self.start_round,
            width=20
        ).pack(pady=10)

        tk.Button(
            self,
            text="Back",
            command=self.app.show_welcome,
            width=20
        ).pack()

    def start_round(self):
        self.app.current_course = self.course

        self.app.current_round = Round(self.course)

        self.app.show_round_entry()