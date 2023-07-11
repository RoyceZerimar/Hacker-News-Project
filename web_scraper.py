import requests
from bs4 import BeautifulSoup

# instead of using .storyline use .titleline.

res = requests.get('https://news.ycombinator.com/news')
# here we grave the html info from the website.
soup = BeautifulSoup(res.text, "html.parser")

# 'a' tags are all the links, the '#' symbol stands for 'id', '.' means it's a class
links = soup.select('.titleline > a')
# print(links)
votes = soup.select('.score')



def create_custom_hn(links, votes):  # a link in html id 'href'
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href')
        hn.append({'link': href, 'title': title})

    return hn


print(create_custom_hn(links, votes))
