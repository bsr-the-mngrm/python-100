import requests
import spotipy
from bs4 import BeautifulSoup
from datetime import datetime
from os import system
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

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


def get_song_list(date: str) -> list:
    """
        Returns a list of songs
        (elements are dict type e.g.: {"title": "Hit Em Up", "artist": "2pac"})
        - Webscraping Billboard Hot100 on the given date
    """

    response = requests.get(f"{BILLBOARD_URL}/{date}")
    billboard_soup = BeautifulSoup(response.text, 'html.parser')

    song_list = []

    for song_title in billboard_soup.select("li ul li h3"):
        song_list.append({"title": str(song_title.getText()).strip().replace("'", " ")})

    song_list[0]['artist'] = str(billboard_soup.find(class_="c-label a-no-trucate a-font-primary-s "
                                                            "lrv-u-font-size-14@mobile-max u-line-height-normal"
                                                            "@mobile-max u-letter-spacing-0021 lrv-u-display-block "
                                                            "a-truncate-ellipsis-2line u-max-width-330 u-max-width-"
                                                            "230@tablet-only u-font-size-20@tablet").getText()
                                 ).strip().replace("'", " ")

    song_artists = billboard_soup.find_all(class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max "
                                                  "u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-"
                                                  "block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230"
                                                  "@tablet-only")

    idx = 1
    for song_artist in song_artists:
        song_list[idx]["artist"] = str(song_artist.getText()).strip().replace("'", " ")
        idx += 1

    return song_list


def get_song_uri_list(sp_api: spotipy.Spotify, song_list: list) -> list:
    """Returns a list of Spotify URIs of the given song titles"""
    song_uri_list = []
    for song in song_list:
        try:
            song_uri_list.append(sp.search(f"track:{song['title']} artist:{song['artist']}")
                                 ['tracks']['items'][0]['uri'])
            print(f"'{song['title']}' (by {song['artist']}) found.")
        except IndexError:
            print(f"'{song['title']}' (by {song['artist']}) not found on Spotify.")

    return song_uri_list


if __name__ == '__main__':
    selected_date = user_input()

    sp = get_spotify_api_client()
    user_id = sp.current_user()['id']

    songs = get_song_list(selected_date)
    song_URIs = get_song_uri_list(sp, songs)

    playlist_name = f"Billboard Hot 100 of {selected_date}"
    playlist_id = sp.user_playlist_create(user_id, playlist_name, public=False,
                                          collaborative=False, description="")['id']

    sp.playlist_add_items(playlist_id, song_URIs)
    print(f"\n'{playlist_name}' is created. Tracks are added.")
