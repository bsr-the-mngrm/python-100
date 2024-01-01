import requests
from bs4 import BeautifulSoup, element
from functools import total_ordering

URL = "https://news.ycombinator.com/"


@total_ordering
class Story:
    def __init__(self, title: str, link: str, upvote: int = 0):
        self.title = title
        self.link = link
        self.upvote = upvote

    def __repr__(self):
        return self.story_to_text()

    def story_to_text(self) -> str:
        return f"Title: {self.title} ({self.link}) - {self.upvote} points"

    def __eq__(self, other):
        return self.upvote == other.upvote

    def __lt__(self, other):
        return self.upvote < other.upvote

    def __gt__(self, other):
        return self.upvote > other.upvote

    def __le__(self, other):
        return self.upvote <= other.upvote

    def __ge__(self, other):
        return self.upvote >= other.upvote


if __name__ == '__main__':
    response = requests.get(URL)
    yc_web_page = response.text

    soup = BeautifulSoup(yc_web_page, "html.parser")

    # # Solution1
    # title_line = soup.select(".titleline a")
    # story_title = [title.getText() for title in title_line if "from?site=" not in title.get("href")]
    # story_link = [title.get("href") for title in title_line if "from?site=" not in title.get("href")]
    # story_upvote = [score.getText() for score in soup.select(".score")]
    #
    # print(story_title)
    # print(story_link)
    # print(story_upvote)

    # Solution2 - Try to get an O(n) solution
    # There aren't tags to iterate over the table which contains the articles so there is only O(n*2) solution
    # stories = []
    # stories_upvote = [score.getText() for score in soup.select(".score")]
    # # for item in soup.find_all(name="td", class_="subtext"):
    # #     print(item.find(name="span", class_="score").getText())
    #
    # idx = 0
    # for item in soup.find_all(name="td", class_="title"):
    #     title_span = item.find(name="span", class_="titleline")
    #     if title_span:
    #         title = title_span.find(name="a").getText()
    #         link = title_span.find(name="a").get("href")
    #         upvote = stories_upvote[idx]
    #
    #         stories.append(Story(title, link, upvote))
    #         idx += 1
    #
    # for story in stories:
    #     print(story.story_to_text())

    # Solution3 - Finally! I found the solution of how to reach O(n)
    stories = []
    title_line = None
    score = None
    idx = 0

    for item in soup.find_all(name="table")[2]:
        # print(type(item))
        # print(item)
        if isinstance(item, element.Tag):
            title_line = item.find(name="span", class_="titleline")
            score = item.find(name="span", class_="score")

            if title_line is not None:
                stories.append(Story(title_line.find(name="a").getText(), title_line.find(name="a").get("href")))
                title_line = None

            if score is not None:
                stories[idx].upvote = int(score.getText().split(' ')[0])
                score = None
                idx += 1

    for story in sorted(stories, reverse=True):
        print(story.story_to_text())
