import pandas


def generate_phonetic():
    # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    user_input = input("Enter a word: ").upper()
    user_input_chars = [char for char in user_input]

    # TODO 3. Add exception handling: if there is a non-alfabet character in the input catch the KeyError exception
    try:
        user_input_with_codes = {letter: nato_alphabet_dict[letter.upper()] for letter in user_input_chars}
    except KeyError:
        print("Only letters are acceptable!")
        generate_phonetic()
    else:
        print(user_input_with_codes)


if __name__ == '__main__':
    print("Welcome to NATO Alphabet Project")

    # TODO 1. Create a dictionary in this format:
    # {"A": "Alfa", "B": "Bravo"}
    nato_alphabet_df = pandas.read_csv("csv/nato_phonetic_alphabet.csv")
    nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet_df.iterrows()}

    generate_phonetic()
