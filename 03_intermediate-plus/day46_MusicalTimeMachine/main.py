import requests
import spotipy
from pprint import pprint
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
            user_choice = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: \n")
            date_format = '%Y-%m-%d'
            if user_choice != "":
                date_obj = datetime.strptime(user_choice, date_format)
            else:
                print("We will go with default value: 2000-08-12\n")
                return '2000-08-12'
        except ValueError:
            system("cls||clear")
            print("Invalid date format! Try again:")
        else:
            return user_choice


def get_song_titles(date: str) -> list:
    """
        Returns a list of sing titles
        - Webscraping Billboard Hot100 on the given date
    """

    response = requests.get(f"{BILLBOARD_URL}/{date}")
    billboard_soup = BeautifulSoup(response.text, 'html.parser')
    song_title_list = [str(song.getText()).strip().replace("'", " ") for song in billboard_soup.select("li ul li h3")]

    return song_title_list


def get_spotify_api_client() -> spotipy.Spotify:
    """Returns a Spotify API client"""
    load_dotenv()
    auth_manager = SpotifyClientCredentials()
    scope = "playlist-modify-public"

    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


if __name__ == '__main__':
    selected_date = user_input()
    song_titles = get_song_titles(selected_date)
    sp = get_spotify_api_client()
