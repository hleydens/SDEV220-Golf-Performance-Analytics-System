from tkinter import *

from src.screens.base_screen import BaseScreen


class WelcomeScreen(BaseScreen):

    def __init__(self, app):

        super().__init__(app)

        Label(
            self,
            text="Golf Performance Analytics System",
            font=("Arial", 22, "bold")
        ).pack(pady=40)

        Button(
            self,
            text="Start New Round",
            width=30,
            command=self.app.show_start_round
        ).pack(pady=8)

        Button(
            self,
            text="View Round History",
            width=30,
            command=self.app.show_round_history
        ).pack(pady=8)

        Button(
            self,
            text="Manage Courses",
            width=30,
            comman=self.app.show_manage_courses
        ).pack(pady=8)

        Button(
            self,
            text="Exit",
            width=30,
            command=self.app.root.destroy
        ).pack(pady=25)