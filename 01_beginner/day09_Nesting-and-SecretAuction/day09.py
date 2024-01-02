# DAY 09 - The Secret Auction

from art import logo
from os import system

secret_auction = {}
is_there_bidder = True

def find_the_highest_bid(bidding_record):
    winner_name = ""
    winner_bid = 0

    for name in bidding_record:
        actual_bid = bidding_record[name]
        if actual_bid > winner_bid:
            winner_name = name
            winner_bid = actual_bid

    print(f"The winner is {winner_name} with a bid of ${winner_bid}.")

while is_there_bidder:
    print(logo)
    print("Welcome to the secret auction program.")

    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))

    secret_auction[name] = bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if should_continue == "yes":
        system("cls||clear")
    elif should_continue == "no":
        is_there_bidder = False
        find_the_highest_bid(secret_auction)