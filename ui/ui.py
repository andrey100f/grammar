from ui.automate_ui import AutomateUI
from ui.grammar_ui import GrammarUI


class UI:
    def __init__(self):
        self.__automate_ui = AutomateUI()
        self.__grammar_ui = GrammarUI()

    def display_menu(self):
        while True:
            print("")
            print("(1) Gramatica.")
            print("(2) Automat.")
            print("(x) Iesire.")

            choice = input("Dati optiunea: ")
            if choice == "1":
                self.__grammar_ui.display_grammar_menu()
            elif choice == "2":
                self.__automate_ui.display_automate_menu()
            elif choice == "x":
                break
            else:
                print("Optiune gresita! Reincercati!")
