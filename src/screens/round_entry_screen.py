import tkinter as tk
from tkinter import ttk, messagebox

from src.screens.base_screen import BaseScreen
from src.models.shot import Shot


class RoundEntryScreen(BaseScreen):

    CLUBS = [
        "Driver",
        "3 Wood",
        "5 Wood",
        "4 Iron",
        "5 Iron",
        "6 Iron",
        "7 Iron",
        "8 Iron",
        "9 Iron",
        "PW",
        "GW",
        "SW",
        "LW",
        "Putter"
    ]

    SHOT_TYPES = [
        "Tee Shot",
        "Approach",
        "Chip",
        "Pitch",
        "Putt",
        "Recovery"
    ]

    LIES = [
        "Tee",
        "Fairway",
        "Rough",
        "Green",
        "Sand",
        "Recovery"
    ]

    def __init__(self, app):
        super().__init__(app)

        self.current_round = self.app.current_round

        self.current_hole = self.current_round.get_current_hole()

        # -------------------------------------------------
        # Header
        # -------------------------------------------------

        tk.Label(
            self,
            text=self.current_round.course.name,
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        self.hole_label = tk.Label(
            self,
            font=("Arial", 16)
        )
        self.hole_label.pack()

        self.par_label = tk.Label(
            self,
            font=("Arial", 12)
        )
        self.par_label.pack()

        self.shot_label = tk.Label(
            self,
            font=("Arial", 14, "bold")
        )
        self.shot_label.pack(pady=(5, 15))

        # -------------------------------------------------
        # Club
        # -------------------------------------------------

        tk.Label(self, text="Club").pack()

        self.club_box = ttk.Combobox(
            self,
            values=self.CLUBS,
            state="readonly",
            width=20
        )

        self.club_box.current(0)

        self.club_box.pack()

        # -------------------------------------------------
        # Shot Type
        # -------------------------------------------------

        tk.Label(self, text="Shot Type").pack(pady=(10, 0))

        self.type_box = ttk.Combobox(
            self,
            values=self.SHOT_TYPES,
            state="readonly",
            width=20
        )

        self.type_box.current(0)

        self.type_box.pack()

        # -------------------------------------------------
        # Lie
        # -------------------------------------------------

        tk.Label(self, text="Lie").pack(pady=(10, 0))

        self.lie_box = ttk.Combobox(
            self,
            values=self.LIES,
            state="readonly",
            width=20
        )

        self.lie_box.current(0)

        self.lie_box.pack()

        # -------------------------------------------------
        # Distance
        # -------------------------------------------------

        tk.Label(
            self,
            text="Distance to Hole (yards)"
        ).pack(pady=(10, 0))

        self.distance_entry = tk.Entry(
            self,
            width=15
        )

        self.distance_entry.pack()

        # -------------------------------------------------
        # Penalty
        # -------------------------------------------------

        self.penalty_var = tk.BooleanVar()

        tk.Checkbutton(
            self,
            text="Penalty",
            variable=self.penalty_var
        ).pack(pady=10)

        # -------------------------------------------------
        # Notes
        # -------------------------------------------------

        tk.Label(
            self,
            text="Notes"
        ).pack()

        self.notes_entry = tk.Entry(
            self,
            width=40
        )

        self.notes_entry.pack()

        # -------------------------------------------------
        # Buttons
        # -------------------------------------------------

        tk.Button(
            self,
            text="Save Shot",
            width=18,
            command=self.save_shot
        ).pack(pady=10)

        tk.Button(
            self,
            text="Hole Out",
            width=18,
            command=self.hole_out
        ).pack()

        self.refresh_screen()

    # -------------------------------------------------

    def refresh_screen(self):

        self.current_hole = self.current_round.get_current_hole()

        self.hole_label.config(
            text=f"Hole {self.current_hole.hole_number}"
        )

        self.par_label.config(
            text=f"Par {self.current_hole.par}"
        )

        self.shot_label.config(
            text=f"Shot #{self.current_hole.get_next_shot_number()}"
        )

        self.clear_inputs()

    def clear_inputs(self):

        self.distance_entry.delete(0, tk.END)

        self.notes_entry.delete(0, tk.END)

        self.penalty_var.set(False)

        self.club_box.current(0)

        self.type_box.current(0)

        self.lie_box.current(0)

    # -------------------------------------------------

    def save_shot(self):

        current_hole = self.current_round.get_current_hole()

    # Validate distance
        try:
            distance = float(self.distance_entry.get())
        except ValueError:
            messagebox.showerror(
                "Invalid Distance",
                "Please enter a valid distance."
            )
            return

        shot = Shot(
            shot_number=current_hole.get_next_shot_number(),
            club=self.club_box.get(),
            shot_type=self.type_box.get(),
            lie=self.lie_box.get(),
            starting_distance=distance,
            penalty=self.penalty_var.get(),
            notes=self.notes_entry.get()
        )

        current_hole.add_shot(shot)

        self.clear_inputs()

        self.refresh_screen()

    # -------------------------------------------------

    def hole_out(self):

        current_hole = self.current_round.get_current_hole()

        if current_hole.get_score() == 0:
            messagebox.showwarning(
                "No Shots",
                "You must record at least one shot before completing the hole."
            )
            return

        has_next_hole = self.current_round.complete_current_hole()

        if has_next_hole:
            self.refresh_screen()
        else:
            messagebox.showinfo(
                "Round Complete",
                "Congratulations! You have finished your round."
            )

            self.app.show_round_summary()