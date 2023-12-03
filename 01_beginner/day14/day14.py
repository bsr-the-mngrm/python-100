from art import logo, vs
from game_data import data
from os import system
from random import randint

LENGTH_OF_DATA = len(data)

# VIEW
def display_round(a_entity, b_entity, score):
    """Displays the next round to the terminal - prints out the logo, the 'A' entity, the 'B' entity and the score if it's greater than zero."""
    system("cls||clear")

    print(logo)
    
    if score > 0:
        print(f"You're right! Current score: {score}\n")
    
    print(f"Compare A: {a_entity['name']} ({a_entity['country']}) - {a_entity['description']}")
    print(vs)
    print(f"Against B: {b_entity['name']} ({b_entity['country']}) - {b_entity['description']}\n")

def display_final(a_entity, b_entity, score):
    """Displays the results to the terminal - prints out the logo, the 'A' entity's follower count, the 'B' entity's follower count and the user's final score"""
    system("cls||clear")
    
    print(logo)
    if score != LENGTH_OF_DATA-1:
        print(f"Wrong answer!\n{a_entity['name']} has {a_entity['follower_count']} followers vs. {b_entity['name']} has {b_entity['follower_count']}\n")
    else:
        print(f"Wow! You did it! Guessed out everything!")
    print(f"Your final score is {score}\n")

def input_answer():
    """Returns 'A' or 'B' depends on the user's choice"""
    input_str = "Who has more followers? Type 'A' or 'B': "
    answer = input(input_str).capitalize()

    while answer != 'A' and answer != 'B':
        answer = input("Only 'A' and 'B' characters acceptable! " + input_str)

    return answer.capitalize()

def input_wants_to_play():
    """Returns 'y' or 'n' depending on whether the user wants to play or not."""
    input_str = "Do you want to play again? Type 'y' to continue or type 'n' to exit: "
    wants_to_play = input(input_str)
    while wants_to_play.lower() != "y" and wants_to_play.lower() != "n":
        wants_to_play = input("Wrong answer! " + input_str)
    return wants_to_play.lower()

# BUSINESS LAYER
def get_the_next_entity(list_of_selected_entities):
    """Returns an index which hasn't been selected yet"""
    next_idx = randint(0,LENGTH_OF_DATA-1)
    while next_idx in list_of_selected_entities:
        next_idx = randint(0,LENGTH_OF_DATA-1)

    return next_idx

def compare(a_entity, b_entity, answer):
    """Returns Higher (True) or Lower (False) depends on the right answer"""
    if a_entity['follower_count'] > b_entity['follower_count']:
        return answer == 'A'
    else:
        return answer == 'B'

def play_game():
    """Play Higher/Lower game"""
    list_of_selected_entities = []
    score = 0
    is_higher = True
    a_entity = {}
    b_entity = {}
    a_entity_idx = 0
    
    #initialization of list of selected entities
    list_of_selected_entities.append(get_the_next_entity(list_of_selected_entities))

    while is_higher and score != LENGTH_OF_DATA-1:
        list_of_selected_entities.append(get_the_next_entity(list_of_selected_entities))

        lenght_of_list_of_selected_entities = len(list_of_selected_entities)
        a_entity = data[list_of_selected_entities[a_entity_idx]]
        b_entity = data[list_of_selected_entities[lenght_of_list_of_selected_entities-1]]

        display_round(a_entity=a_entity, b_entity=b_entity, score=score)

        choice = input_answer()

        if compare(a_entity=a_entity, b_entity=b_entity, answer=choice):
            score += 1
            if choice == 'B':
                a_entity_idx = lenght_of_list_of_selected_entities - 1
        else:
            is_higher = False

    display_final(a_entity=a_entity, b_entity=b_entity, score=score)
    

# Main
wants_to_play = 'y'

while wants_to_play == 'y':
    play_game()
    wants_to_play = input_wants_to_play()