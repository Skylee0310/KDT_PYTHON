from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs) # 전체 html 코드를 모두 가지고 있음.
print(bs.h1)
print(bs.h1.string) #.text (Deprecated) -> .string : 태그 내부의 문자열만 가져옴.

print(bs.title)
print('title:', bs.title.string)