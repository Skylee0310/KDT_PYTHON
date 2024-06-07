from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages = set() # 동일한 페이지를 두 번 크롤링 하는 것을 방지한다.
count=0
def getLinks(pageUrl):
    global pages
    global count
    html = urlopen('https://en.wikipedia.org{}'.format(pageUrl)) #('https://en.wikipedia.org{0}.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    try :
        print(bs.h1.get_text())
        print(bs.find(id='mw-content-text').find('p').text)
    except AttributeError as e :
        print('this page is missing something! Continuing: ', e)

    for link in bs.find_all('a', href=re.compile('^(/wiki/)')): #^정규식의 시작을 나타냄.
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages :
                # 새로운 페이지 발견.
                newPage = link.attrs['href']
                count +=1
                print(f'[{count}] : {newPage}')
                pages.add(newPage) #세트에 추가.
                getLinks(newPage) #재귀호출.

getLinks('')