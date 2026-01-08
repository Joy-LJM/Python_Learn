from bs4 import BeautifulSoup

with open("website.html") as file:
    contents=file.read()

soup=BeautifulSoup(contents, "html.parser")

print(soup)
print(soup.prettify())
print(soup.title.string)

all_anchor_tags=soup.find_all('a')
for anchor in all_anchor_tags:
    print(anchor.get('href'))

h3_heading=soup.find_all("h3",class_="heading")
print(h3_heading)

heading=soup.select('.heading')
print(heading)

name=soup.select_one('#name')
print(name)

class_is_heading=soup.find_all(class_="heading")
print(class_is_heading)

tag=soup.select("p a")
print(tag)


