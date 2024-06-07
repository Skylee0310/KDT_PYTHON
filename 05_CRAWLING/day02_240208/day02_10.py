from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import re

#random.seed(datatime.datetime.now())
random.seed(None)

def getLinks(articleUrl):
    html = urlopen('https://en.wikipedia.org'+articleUrl)
    bs = BeautifulSoup(html, 'html.parser')
    bodyContent = bs.find('div', {"id" : 'bodyContent'})
    wikiUrl = bodyContent.find_all('a', href = re.compile('^(/wiki/)((?!:).)*$'))
    return wikiUrl

link = getLinks('/wiki/Kevin_Bacon')
print('link 길이 : ', len(link))
while len(link) >0 :
    newArticle = link[random.randint(0, len(link)-1)].attrs['href']
    print(newArticle)
    link=getLinks(newArticle)