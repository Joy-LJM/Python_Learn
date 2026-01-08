import requests
from bs4 import BeautifulSoup

movies_res=requests.get("https://www.timeout.com/film/best-movies-of-all-time")
movies_soup=BeautifulSoup(movies_res.text,'html.parser')

movies=movies_soup.find_all(name='h3', attrs={"data-testid":"tile-title_testID"})
movies.pop(len(movies)-1)

with open('top100_movies.txt','w',encoding='utf-8') as file:
    for movie in movies[::-1]:
        name=movie.text.replace(' ','')
        file.write(f'{name}\n')