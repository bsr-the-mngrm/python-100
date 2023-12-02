from art import logo, vs
from game_data import data
from os import system
from random import randint

LENGTH_OF_DATA = len(data)

# get the next entity index
def get_the_next_entity(list_of_selected_entities):
    next_idx = randint(0,LENGTH_OF_DATA-1)
    while next_idx in list_of_selected_entities:
        next_idx = randint(0,LENGTH_OF_DATA-1)

    return next_idx

# user inputs

def input_wants_to_play():
    pass

# comperation

# play game
def play_game():
    list_of_selected_entities = []
    
    #initialization of list of selected entities
    list_of_selected_entities.append(get_the_next_entity(list_of_selected_entities))

    print(logo)

    list_of_selected_entities.append(get_the_next_entity(list_of_selected_entities))

    print(list_of_selected_entities)



# main

wants_to_play = 'y'

while wants_to_play == 'y':
    play_game()
    wants_to_play = input_wants_to_play()