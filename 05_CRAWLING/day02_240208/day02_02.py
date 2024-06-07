from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html, 'html.parser')

#등장인물의 이름 : 녹색
namelist = soup.find_all('span', {'class':'green'})
print('[등장인물 이름]')
for name in namelist :
    print(name.string)
print('-'*80)

