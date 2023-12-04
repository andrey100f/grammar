from automate.transition import Transition


class Automate:
    def __init__(self):
        self.__states = []
        self.__alphabet = []
        self.__transitions = []
        self.__initial_state = None
        self.__final_state = None

    def config_automate_from_grammar(self, states, alphabet, transitions, initial_state, final_state, filename):
        # Configuram automatul
        for letter in alphabet:
            self.__alphabet.append(letter)
        for state in states:
            self.__states.append(state)
        for transition in transitions:
            self.__transitions.append(transition)
        self.__initial_state = initial_state
        self.__final_state = final_state

        # Cream fisierul de configurare
        self.__create_config_file(filename)

    def __create_config_file(self, filename):
        with open(filename, "w") as file:
            # Scriem alfabetul
            line = ""
            for letter in self.__alphabet:
                line += letter
                line += " "
            line = line.strip()
            file.write(line)
            file.write("\n")

            # Scriem starile
            line = ""
            for state in self.__states:
                line += state
                line += " "
            line = line.strip()
            file.write(line)
            file.write("\n")

            # Scriem starea initiala
            file.write(self.__initial_state)
            file.write("\n")

            # Scriem starea finala
            file.write(self.__final_state)
            file.write("\n")

            # Scriem tranzitiile
            for transition in self.__transitions:
                line = str(transition)
                file.write(line)
                file.write("\n")

    def config_automate_from_file(self, filename):
        with open(filename, "r") as file:
            line_number = 0
            for line in file:
                line_number += 1
                if line_number == 1:
                    self.__add_elements(line, "alphabet")
                elif line_number == 2:
                    self.__add_elements(line, "states")
                elif line_number == 3:
                    line = line.strip("\n")
                    self.__initial_state = line
                elif line_number == 4:
                    line = line.strip("\n")
                    self.__final_state = line
                else:
                    self.__add_transitions(line)

    def __add_elements(self, line, list_to_add):
        line = line.strip("\n")
        terminals = line.split(" ")

        if list_to_add == "alphabet":
            grammar_element = self.__alphabet
        else:
            grammar_element = self.__states

        for terminal in terminals:
            grammar_element.append(terminal)

    def __add_transitions(self, line):
        line = line.strip("\n")
        transition = Transition()
        transition.set_transition(line)
        self.__transitions.append(transition)

    def get_alphabet(self):
        return self.__alphabet

    def get_states(self):
        return self.__states

    def get_initial_state(self):
        return self.__initial_state

    def get_final_state(self):
        return self.__final_state

    def get_transitions(self):
        return self.__transitions
