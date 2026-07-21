from tkinter import *

from src.screens.base_screen import BaseScreen

from src.models.golfer import Golfer


class ManageGolfersScreen(BaseScreen):

    def __init__(self, app):

        super().__init__(app)

        Label(
            self,
            text="Manage Golfers",
            font=("Arial",20,"bold")
        ).pack(pady=20)

        self.name_entry = Entry(
            self,
            width=30
        )

        self.name_entry.pack(pady=10)

        Button(
            self,
            text="Add Golfer",
            command=self.add_golfer
        ).pack()

        self.golfer_list = Listbox(
            self,
            width=40,
            height=12
        )

        self.golfer_list.pack(pady=20)

        Button(
            self,
            text="Back",
            command=self.app.show_welcome
        ).pack()

    def add_golfer(self):

        name = self.name_entry.get().strip()

        if name == "":
            return

        golfer = Golfer(name)

        self.app.storage.add_golfer(golfer)

        self.golfer_list.insert(END,name)

        self.name_entry.delete(0,END)