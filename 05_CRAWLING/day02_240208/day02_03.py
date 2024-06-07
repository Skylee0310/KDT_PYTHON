from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

princeList = soup.find_all(string='the prince')
print('[특정 단어(the prince) 찾기 => find_all(text = "검색어")]')
print(princeList)
print('the prince count: ', len(princeList))
print('-'*80)

table_tag = soup.find('table', {'id' : 'giftList'})
print('children 개수 : ', len(list(table_tag.children)))
for child in table_tag.children :
    print(child)
    print('-'*30)


desc =soup.find('table',{'id': 'giftList'}).descendants
list_desc = list(desc)
print('descendants 개수 : ', len(list_desc))

for tag in list_desc :
    print(tag)

#next_sibling속성.
for sibling in soup.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)

sibling1 = soup.find('tr', {'id':'gift3'}).next_sibling
print('sibling1:', sibling1)
print('ord(sibling1)):', ord(sibling1))
print()
sibling2 = soup.find('tr', {'id':'gift3'}).next_sibling.nextSibling
print(sibling2)

img1 = soup.find('img', {'src': '../img/gifts/img1.jpg'})
text = img1.parent.previous_sibling.get_text()
print(text)