import pandas


if __name__ == '__main__':
    print("Welcome to NATO Alphabet Project")

    # TODO 1. Create a dictionary in this format:
    # {"A": "Alfa", "B": "Bravo"}
    nato_alphabet_df = pandas.read_csv("csv/nato_phonetic_alphabet.csv")
    nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet_df.iterrows()}

    # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    user_input = input("Write a word: ")
    user_input_letters = [letter for letter in user_input]
    user_input_with_codes = {letter: nato_alphabet_dict[letter.upper()] for letter in user_input_letters}

    print(user_input_with_codes)
