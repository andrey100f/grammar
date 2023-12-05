from grammar.grammar import Grammar


class GrammarUI:
    def __init__(self):
        self.__grammar = None

    def display_grammar_menu(self):
        while True:
            print("")
            print("(1) Configurare gramatica din fisier.")
            print("(2) Afisare terminale.")
            print("(3) Afisare non-terminale.")
            print("(4) Afisare productii.")
            print("(5) Afisare productii ale unui non-terminal.")
            print("(6) Afisare simbol de start.")
            print("(7) Afisare simbol final.")
            print("(8) Verificare gramatica regulara.")
            print("(9) Conversie in automat.")
            print("(x) Mergi inapoi.")

            choice = input("Dati optiunea: ")
            if choice == "1":
                filename = "grammar/grammar_config.txt"
                self.__grammar = Grammar()
                self.__grammar.config_grammar_from_file(filename)

                print(f"Gramatica a fost configurata folosind fisierul: {filename}")
            elif choice == "2":
                if self.__grammar is None:
                    print("Gramatica nu a fost configurata!!")
                else:
                    terminals = self.__grammar.get_terminals()

                    print(f"Multimea terminalelor este: {terminals}")
            elif choice == "3":
                if self.__grammar is None:
                    print("Gramatica nu a fost configurata!!")
                else:
                    non_terminals = self.__grammar.get_non_terminals()

                    print(f"Multimea non-terminalelor este: {non_terminals}")
            elif choice == "4":
                if self.__grammar is None:
                    print("Gramatica nu a fost configurata!!")
                else:
                    productions = self.__grammar.get_productions()

                    print("Multimea productiilor este: ")
                    for production in productions:
                        print(production)
            elif choice == "5":
                if self.__grammar is None:
                    print("Gramatica nu a fost configurata!!")
                else:
                    non_terminal = input("Dati non-terminalul: ")

                    production = self.__grammar.get_production_by_non_terminal(non_terminal)

                    if production is None:
                        print("Non-terminalul nu este valid!!")
                    else:
                        print(f"Productia este: {production}")
            elif choice == "6":
                if self.__grammar is None:
                    print("Gramatica nu a fost configurata!!")
                else:
                    start_symbol = self.__grammar.get_start_symbol()

                    print(f"Simbolul de start este: {start_symbol}")
            elif choice == "7":
                if self.__grammar is None:
                    print("Gramatica nu a fost configurata!!")
                else:
                    end_symbol = self.__grammar.get_end_symbol()

                    print(f"Simbolul de final este: {end_symbol}")
            elif choice == "8":
                if self.__grammar is None:
                    print("Gramatica nu a fost configurata!!")
                else:
                    is_regular = self.__grammar.check_regular()

                    if is_regular is True:
                        print("Gramatica este regulara!!")
                    else:
                        print("Granatica nu este regulara!!")
            elif choice == "9":
                if self.__grammar is None:
                    print("Gramatica nu a fost configurata!!")
                else:
                    filename = "grammar/result_automate_config.txt"
                    automate = self.__grammar.convert_to_finite_automate(filename)

                    print(f"Fisierul de configurare pentru automatul generat este: {filename}")
                    print("Automatul generat este: ")
                    automate.print_automate()
            elif choice == "x":
                break
            else:
                print("Optiune gresita!! Reincercati...")
