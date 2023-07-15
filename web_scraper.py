import requests
from bs4 import BeautifulSoup
import pprint

# instead of using .storyline use .titleline.

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
# here we grave the html info from the website.
soup = BeautifulSoup(res.text, "html.parser")
soup2 = BeautifulSoup(res2.text, "html.parser")

# 'a' tags are all the links, the '#' symbol stands for 'id', '.' means it's a class
links = soup.select('.titleline > a')
# print(links)
subtext = soup.select('.subtext')

links2 = soup2.select('.titleline > a')
# print(links)
subtext2 = soup2.select('.subtext')


mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(hnList):
    return sorted(hnList, key=lambda k: k["votes"], reverse=True)


def create_custom_hn(links, subtext):  # a link in html id 'href'
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText(). replace("points", ""))
            if points > 99:
                # print(points)
                hn.append({"title": title, "link": href, "votes": points})

    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
