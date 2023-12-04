from grammar.grammar import Grammar


def main():
    filename = "grammar/grammar_config.txt"
    grammar = Grammar(filename)
    grammar.convert_to_finite_automate("automate/automate_config.txt")


if __name__ == '__main__':
    main()
