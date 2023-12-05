from automate.automate import Automate


class AutomateUI:
    def __init__(self):
        self.__automate = None

    def display_automate_menu(self):
        while True:
            print("")
            print("(1) Configurare automat din fisier.")
            print("(2) Afisare multime stari.")
            print("(3) Afisare alfabet.")
            print("(4) Afisare tranzitii.")
            print("(5) Afisare stare initiala.")
            print("(6) Afisare stare finala.")
            print("(7) Afisare stare urmatoare.")
            print("(8) Verificare secventa.")
            print("(9) Conversie in gramatica.")
            print("(x) Mergi inapoi.")

            choice = input("Dati optiunea: ")
            if choice == "1":
                filename = "automate/automate_config.txt"
                self.__automate = Automate()
                self.__automate.config_automate_from_file(filename)

                print(f"Automatul a fost configurat folosind fisierul: {filename}")
            elif choice == "2":
                if self.__automate is None:
                    print("Automatul nu a fost configurat!!")
                else:
                    states = self.__automate.get_states()

                    print(f"Multimea starilor este: {states}")
            elif choice == "3":
                if self.__automate is None:
                    print("Automatul nu a fost configurat!!")
                else:
                    alphabet = self.__automate.get_alphabet()

                    print(f"Alfabetul este: {alphabet}")
            elif choice == "4":
                if self.__automate is None:
                    print("Automatul nu a fost configurat!!")
                else:
                    transitions = self.__automate.get_transitions()

                    print("Multimea tranzitiilor este: ")
                    for transition in transitions:
                        print(transition)
            elif choice == "5":
                if self.__automate is None:
                    print("Automatul nu a fost configurat!!")
                else:
                    initial_state = self.__automate.get_initial_state()

                    print(f"Starea initiala este: {initial_state}")
            elif choice == "6":
                if self.__automate is None:
                    print("Automatul nu a fost configurat!!")
                else:
                    final_state = self.__automate.get_final_state()

                    print(f"Starea finala este: {final_state}")
            elif choice == "7":
                if self.__automate is None:
                    print("Automatul nu a fost configurat!!")
                else:
                    source_state = input("Dati starea initiala: ")
                    symbol = input("Dati simbolul: ")

                    next_state = self.__automate.get_next_state(source_state, symbol)

                    if len(next_state) == 0:
                        print("Input-ul nu este valid!!")
                    else:
                        print(f"Starile urmatoare sunt: {next_state}")
            elif choice == "8":
                if self.__automate is None:
                    print("Automatul nu a fost configurat!!")
                else:
                    sequence = input("Dati secventa: ")

                    is_valid = self.__automate.check_sequence(sequence)

                    if is_valid is True:
                        print("Secventa este valida!!")
                    else:
                        print("Secventa nu este valida!!")
            elif choice == "9":
                if self.__automate is None:
                    print("Automatul nu a fost configurat!!")
                else:
                    filename = "automate/result_grammar_config.txt"
                    grammar = self.__automate.convert_to_grammar(filename)

                    print(f"Fisierul de configurare pentru gramatica generata este: {filename}")
                    print("Gramatica generata este: ")
                    grammar.print_grammar()
            elif choice == "x":
                break
            else:
                print("Optiune gresita!! Reincercati...")
