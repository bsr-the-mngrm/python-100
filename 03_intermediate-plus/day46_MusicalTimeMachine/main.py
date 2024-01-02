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


def get_spotify_api_client() -> spotipy.Spotify:
    """Returns a Spotify API client"""
    load_dotenv()
    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            show_dialog=True,
            cache_path=".data/token.txt"
        )
    )


def get_song_titles(date: str) -> list:
    """
        Returns a list of sing titles
        - Webscraping Billboard Hot100 on the given date
    """

    response = requests.get(f"{BILLBOARD_URL}/{date}")
    billboard_soup = BeautifulSoup(response.text, 'html.parser')
    song_title_list = [str(song.getText()).strip().replace("'", " ") for song in billboard_soup.select("li ul li h3")]

    return song_title_list


def get_song_uri_list(sp_api: spotipy.Spotify, song_title_list: list) -> list:
    """Returns a list of Spotify URIs of the given song titles"""
    song_uri_list = []
    for song_title in song_title_list:
        try:
            song_uri_list.append(sp.search(f"track:{song_title}")['tracks']['items'][0]['uri'])
            print(f"'{song_title}' found on Spotify.")
        except IndexError:
            print(f"'{song_title}' not found on Spotify.")

    return song_uri_list


if __name__ == '__main__':
    selected_date = user_input()

    sp = get_spotify_api_client()
    user_id = sp.current_user()['id']

    song_titles = get_song_titles(selected_date)
    song_URIs = get_song_uri_list(sp, song_titles)

    playlist_name = f"Billboard Hot 100 of {selected_date}"
    playlist_id = sp.user_playlist_create(user_id, playlist_name, public=False,
                                          collaborative=False, description="")['id']
    
    sp.playlist_add_items(playlist_id, song_URIs)
