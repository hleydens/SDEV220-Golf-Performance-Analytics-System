import tkinter as tk
from src.screens.base_screen import BaseScreen


class ManageCoursesScreen(BaseScreen):

    def __init__(self, app):
        super().__init__(app)

        tk.Label(
            self,
            text="Manage Courses",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        tk.Label(
            self,
            text="Course management coming next."
        ).pack()

        tk.Button(
            self,
            text="Back",
            command=self.app.show_welcome
        ).pack(pady=20)