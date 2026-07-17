import tkinter as tk


class MainWindow:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Golf Performance Analytics System")

        self.root.geometry("600x500")

        self.root.resizable(False, False)

        title = tk.Label(
            self.root,
            text="Golf Performance Analytics System",
            font=("Arial", 20, "bold")
        )

        title.pack(pady=30)

        subtitle = tk.Label(
            self.root,
            text="Welcome!",
            font=("Arial", 14)
        )

        subtitle.pack(pady=5)

        tk.Button(
            self.root,
            text="Start New Round",
            width=30,
            height=2
        ).pack(pady=8)

        tk.Button(
            self.root,
            text="View Golfer Statistics",
            width=30,
            height=2
        ).pack(pady=8)

        tk.Button(
            self.root,
            text="Manage Golfers",
            width=30,
            height=2
        ).pack(pady=8)

        tk.Button(
            self.root,
            text="Manage Courses",
            width=30,
            height=2
        ).pack(pady=8)

        tk.Button(
            self.root,
            text="Exit",
            width=30,
            height=2,
            command=self.root.destroy
        ).pack(pady=25)

    def run(self):

        self.root.mainloop()