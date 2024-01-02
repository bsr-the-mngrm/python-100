import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

if __name__ == '__main__':
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    title_elements = soup.find_all(name="h3", class_="title")
    titles = [title.getText() for title in title_elements[::-1]]

    # for i in range(len(title_elements)-1, -1, -1):
    #     titles.append(title_elements[i].getText())

    with open(file=".data/best-movies.txt", mode="w", encoding="utf-8") as text_file:
        for title in titles:
            text_file.write(title + '\n')
