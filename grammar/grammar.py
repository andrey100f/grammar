from grammar.production import Production
from automate.automate import Automate
from automate.transition import Transition


class Grammar:
    def __init__(self, filename):
        self.__filename = filename
        self.__non_terminals = []
        self.__terminals = []
        self.__productions = []
        self.__start_symbol = None
        self.__end_symbol = None

        self.__config_grammar(filename)

    def __config_grammar(self, filename):
        with open(filename, "r") as file:
            line_number = 0
            for line in file:
                line_number += 1
                if line_number == 1: # we are at the terminals
                    self.add_elements(line, "terminals")
                elif line_number == 2:
                    self.add_elements(line, "non_terminals")
                elif line_number == 3:
                    line = line.strip("\n")
                    self.__start_symbol = line
                elif line_number == 4:
                    line = line.strip("\n")
                    self.__end_symbol = line
                else:
                    self.__add_productions(line)

    def add_elements(self, line, list_to_add):
        line = line.strip("\n")
        terminals = line.split(" ")

        if list_to_add == "terminals":
            grammar_element = self.__terminals
        else:
            grammar_element = self.__non_terminals

        for terminal in terminals:
            grammar_element.append(terminal)

    def __add_productions(self, line):
        line = line.strip("\n")
        production = Production()
        production.set_production(line)
        self.__productions.append(production)

    def get_productions(self):
        return self.__productions

    def get_production_by_non_terminal(self, non_terminal):
        result = None
        for production in self.__productions:
            symbol = production.get_symbol()
            if symbol == non_terminal:
                result = production
        return result

    def get_start_symbol(self):
        return self.__start_symbol

    def get_terminals(self):
        return self.__terminals

    def get_non_terminals(self):
        return self.__non_terminals

    def check_regular(self):
        for production in self.__productions:
            if production.get_symbol() not in self.__non_terminals:
                return False

            for symbol in production.get_values():
                for letter in symbol:
                    if letter not in self.__terminals and letter not in self.__non_terminals:
                        return False

        return True

    def convert_to_finite_automate(self, filename):
        automate = Automate()

        states = []
        for state in self.__non_terminals:
            states.append(state)

        initial_state = self.__start_symbol
        final_state = self.__end_symbol

        alphabet = []
        for letter in self.__terminals:
            alphabet.append(letter)

        transitions = []
        for production in self.__productions:
            for value in production.get_values():
                if len(value) != 1:
                    transition = Transition()
                    line = production.get_symbol() + " " + value[1] + " " + value[0]
                    transition.set_transition(line)
                    transitions.append(transition)
                else:
                    if value in self.__non_terminals:
                        prod = self.get_production_by_non_terminal(value)
                        for val in prod.get_values():
                            if len(val) != 1:
                                transition = Transition()
                                line = production.get_symbol() + " " + val[1] + " " + val[0]
                                transition.set_transition(line)
                                transitions.append(transition)
                            elif val not in self.__non_terminals:
                                transition = Transition()
                                line = production.get_symbol() + " " + val + " " + self.__end_symbol
                                transition.set_transition(line)
                                transitions.append(transition)

        automate.config_automate_from_grammar(states, alphabet, transitions, initial_state, final_state, filename)

        return automate
