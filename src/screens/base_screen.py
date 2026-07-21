import tkinter as tk


class BaseScreen(tk.Frame):

    def __init__(self, app):

        super().__init__(app.root)

        self.app = app