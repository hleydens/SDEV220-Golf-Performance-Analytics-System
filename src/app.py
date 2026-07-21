import tkinter as tk

from src.screens.welcome_screen import WelcomeScreen

from src.storage import StorageManager

from src.screens.manage_golfers_screen import ManageGolfersScreen


class App:
    def __init__(self):
        self.storage = StorageManager()

        self.root = tk.Tk()

        self.root.title("Golf Performance Analytics System")
        self.root.geometry("700x600")
        self.root.resizable(False, False)

        self.current_screen = None

        self.show_welcome()

    def clear_screen(self):
        if self.current_screen:
            self.current_screen.destroy()

    def show_welcome(self):
        self.clear_screen()

        self.current_screen = WelcomeScreen(self)

        self.current_screen.pack(fill="both", expand=True)

    def run(self):
        self.root.mainloop()

    def show_manage_golfers(self):
        self.clear_screen()
        self.current_screen = ManageGolfersScreen(self)
        self.current_screen.pack(fill="both",expand=True)