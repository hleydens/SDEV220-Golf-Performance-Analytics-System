import tkinter as tk
from tkinter import Button, Frame, Label, Listbox, Scrollbar, END, BOTH, LEFT, RIGHT, Y, messagebox


class RoundHistoryScreen(Frame):

    def __init__(self, app):
        super().__init__(app.root)

        self.app = app
        self.rounds = []

        Label(
            self,
            text="Round History",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        Label(
            self,
            text="Select a completed round."
        ).pack()

        list_frame = Frame(self)
        list_frame.pack(fill=BOTH, expand=True, padx=20, pady=15)

        scrollbar = Scrollbar(list_frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.round_list = Listbox(
            list_frame,
            width=70,
            height=15,
            yscrollcommand=scrollbar.set
        )

        self.round_list.pack(
            side=LEFT,
            fill=BOTH,
            expand=True
        )

        scrollbar.config(command=self.round_list.yview)

        button_frame = Frame(self)
        button_frame.pack(pady=10)

        Button(
            button_frame,
            text="View Round",
            width=15,
            command=self.view_round
        ).pack(side=LEFT, padx=5)

        Button(
            button_frame,
            text="Refresh",
            width=15,
            command=self.load_rounds
        ).pack(side=LEFT, padx=5)

        Button(
            button_frame,
            text="Back",
            width=15,
            command=self.app.show_welcome
        ).pack(side=LEFT, padx=5)

        self.load_rounds()

    def load_rounds(self):

        self.round_list.delete(0, END)

        self.rounds = self.app.storage.get_rounds()

        if len(self.rounds) == 0:

            self.round_list.insert(
                END,
                "No completed rounds found."
            )

            return

        for round_obj in reversed(self.rounds):

            score = round_obj.get_total_score()

            to_par = round_obj.get_score_to_par()

            self.round_list.insert(
                END,
                f"{round_obj.date} | "
                f"{round_obj.course.name} | "
                f"Score {score} ({to_par:+})"
            )

    def view_round(self):

        selection = self.round_list.curselection()

        if not selection:

            messagebox.showwarning(
                "No Selection",
                "Please select a round."
            )

            return

        index = len(self.rounds) - 1 - selection[0]

        self.app.selected_round = self.rounds[index]

        self.app.show_round_analysis()