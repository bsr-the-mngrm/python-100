import requests
import spotipy
from bs4 import BeautifulSoup
from datetime import datetime
from os import system
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"


def user_input() -> str:
    """Give back a date (str) in valid format (YYYY-MM-DD)"""
    user_choice = None
    while user_choice != "":
        try:
            user_choice = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: \n"
                                "(do not write anything and hit 'Enter' to exit) \n")
            date_format = '%Y-%m-%d'
            if user_choice != "":
                date_obj = datetime.strptime(user_choice, date_format)
        except ValueError:
            system("cls||clear")
            print("Invalid date format! Try again:")
        else:
            return user_choice

    return user_choice


if __name__ == '__main__':
    pass
