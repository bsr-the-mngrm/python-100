PLACEHOLDER = "[name]"


def open_starting_letter():
    letter = ""

    with open("Input/Letters/starting_letter.txt") as file:
        letter = file.read()

    return letter


def open_invited_names():
    names = []
    with open("Input/Names/invited_names.txt") as file:
        for name in file.readlines():
            new_name = name.strip()
            names.append(new_name)

    return names


def write_letters(letter: str, names: list):
    for name in names:
        new_letter = letter.replace(PLACEHOLDER, name)
        with open(f"Output/ReadyToSend/letter_to_{name.lower()}", mode="w") as file:
            file.write(new_letter)


if __name__ == '__main__':
    starting_letter = open_starting_letter()
    print("starting_letter.txt loaded\n")

    invited_names = open_invited_names()
    print("invited_names.txt loaded\n")

    write_letters(starting_letter, invited_names)
    print("Letters are written! Check out 'Output/ReadyToSend' folder!")



