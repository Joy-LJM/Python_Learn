from bs4 import BeautifulSoup
import requests

res=requests.get('https://news.ycombinator.com/news')
yc_web_page=res.text

soup=BeautifulSoup(yc_web_page,'html.parser')
article_tags=soup.find_all(name="span",attrs={"class":"titleline"})
article_links=[]
article_titles=[]
for article in article_tags:
    anchor_tag=article.find('a')
    article_text= anchor_tag.getText()
    article_link=anchor_tag.get('href')
    article_titles.append(article_text)
    article_links.append(article_link)



upvotes=[int(score.getText().split()[0]) for score in soup.find_all(name='span',class_="score")]
print(upvotes)
print(article_titles)
print(article_links)
max_vote_article=max(upvotes)
max_vote_index=upvotes.index(max_vote_article)


print(max_vote_article)
print(article_titles[max_vote_index])
print(article_links[max_vote_index])