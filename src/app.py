import tkinter as tk
from src.screens.welcome_screen import WelcomeScreen
from src.storage import StorageManager
from src.screens.manage_courses_screen import ManageCoursesScreen
from src.screens.start_round_screen import StartRoundScreen
from src.screens.round_entry_screen import RoundEntryScreen
from src.screens.round_summary_screen import RoundSummaryScreen
from src.screens.round_history_screen import RoundHistoryScreen
from src.screens.round_analysis_screen import RoundAnalysisScreen
from src.screens.hole_scores_screen import HoleScoresScreen

class App:

    def __init__(self):

        self.storage = StorageManager()
        print(f"Loaded {len(self.storage.get_rounds())} rounds.")

        self.current_round = None
        self.current_course = None
        self.selected_round = None

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

    def show_manage_courses(self):
        self.clear_screen()
        self.current_screen = ManageCoursesScreen(self)
        self.current_screen.pack(fill="both", expand=True)


    def show_start_round(self):
        self.clear_screen()
        self.current_screen = StartRoundScreen(self)
        self.current_screen.pack(fill="both", expand=True)


    def show_round_history(self):
        self.clear_screen()
        self.current_screen = RoundHistoryScreen(self)
        self.current_screen.pack(fill="both", expand=True)


    def show_round_entry(self):
        self.clear_screen()
        self.current_screen = RoundEntryScreen(self)
        self.current_screen.pack(fill="both", expand=True)


    def show_round_summary(self):
        self.clear_screen()
        self.current_screen = RoundSummaryScreen(self)
        self.current_screen.pack(fill="both", expand=True)

    def show_round_analysis(self):
        self.clear_screen()

        self.current_screen = RoundAnalysisScreen(self)

        self.current_screen.pack(fill="both", expand=True)

    def show_hole_scores(self):
        self.clear_screen()
        self.current_screen = HoleScoresScreen(self)
        self.current_screen.pack(fill="both", expand=True)