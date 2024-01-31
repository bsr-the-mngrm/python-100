import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# url = "https://api.themoviedb.org/3/search/movie?query=The Matrix&include_adult=false&language=en-US&page=1"
#
# headers = {
#     "accept": "application/json",
#     "Authorization": f"Bearer {getenv('TMDB_API_KEY')}"
# }
#
# response = requests.get(url, headers=headers)
#
# print(response.json()["results"])

url = "https://api.themoviedb.org/3/movie/603?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {getenv('TMDB_API_KEY')}"
}

response = requests.get(url, headers=headers)

print(response.json())
