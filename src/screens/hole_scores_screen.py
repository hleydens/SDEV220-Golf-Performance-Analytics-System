from tkinter import Frame, Label, Button


class HoleScoresScreen(Frame):

    def __init__(self, app):
        super().__init__(app.root)

        self.app = app
        self.round_obj = app.selected_round

        Label(
            self,
            text="Hole Scores",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        header = Frame(self)
        header.pack(pady=5)

        Label(header, text="Hole", width=8, font=("Arial", 10, "bold")).grid(row=0, column=0)
        Label(header, text="Par", width=8, font=("Arial", 10, "bold")).grid(row=0, column=1)
        Label(header, text="Score", width=8, font=("Arial", 10, "bold")).grid(row=0, column=2)
        Label(header, text="+/-", width=8, font=("Arial", 10, "bold")).grid(row=0, column=3)

        for hole in self.round_obj.holes:

            score = hole.get_score()
            difference = score - hole.par

            if difference == 0:
                diff = "E"
            else:
                diff = f"{difference:+}"

            row = Frame(self)
            row.pack()

            Label(row, text=hole.hole_number, width=8).grid(row=0, column=0)
            Label(row, text=hole.par, width=8).grid(row=0, column=1)
            Label(row, text=score, width=8).grid(row=0, column=2)
            Label(row, text=diff, width=8).grid(row=0, column=3)

        Button(
            self,
            text="Back",
            width=20,
            command=self.app.show_round_analysis
        ).pack(pady=20)