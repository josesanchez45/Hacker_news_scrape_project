import pprint

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
res2= requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')
soup2 = BeautifulSoup(res.text, 'html.parser')
links2 = soup2.select('.titleline > a')
subtext2 = soup2.select('.subtext')

mega_links = links +links2
mega_subtext = subtext + subtext2

def return_sorted_stories_by_vote(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hackernews(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return return_sorted_stories_by_vote(hn)


pprint.pprint(create_custom_hackernews(mega_links, mega_subtext))
