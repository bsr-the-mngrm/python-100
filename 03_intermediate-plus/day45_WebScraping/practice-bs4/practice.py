from bs4 import BeautifulSoup

with open(file="website.html", mode="r", encoding="utf8") as html_file:
    contents = html_file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup)
# print(soup.prettify())

# TASK1
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.get("href"))

# TASK2
heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.name)
print(section_heading.getText())
print(section_heading.get("class"))

# TASK3
company_url = soup.select_one(selector="p a")
print(company_url.get("href"))

name = soup.select_one("#name")
print(name.getText())

headings = [heading.getText() for heading in soup.select(".heading")]
print(headings)

# import lxml
# soup = BeautifulSoup(html_file=contents, parser="lxml")
