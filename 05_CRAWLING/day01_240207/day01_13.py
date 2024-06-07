html_example = '''
 <!DOCTYPE   html>
 <html   lang="en">
 <head>
     <meta   charset="UTF-8">
     <meta   name="viewport"   content="width=device-width,   initial-scale=1.0">
     <title>BeautifulSoup   활용</title>
 </head>
 <body>
     <h1   id="heading">Heading   1</h1>
     <p>Paragraph</p>
     <span   class="red">BeautifulSoup   Library   Examples!</span>
     <div   id="link">
         <a   class="external_link"   href="www.google.com">google</a>
         <div   id="class1">
             <p   id="first">class1's   first   paragraph</p>
             <a   class="external_link"   href="www.naver.com">naver</a>
             <p   id="second">class1's   second   paragraph</p>
             <a   class="internal_link"   href="/pages/page1.html">Page1</a>
             <p   id="third">class1's   third   paragraph</p>
         </div>
     </div>
     <div   id="text_id2">
     Example   page
     <p>g</p>
     </div>
     <h1   id="footer">Footer</h1>
 </body>
 </html>
 '''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_example, 'html.parser')

print(soup.title) #<title> 태그 전체를 가져옴
print(soup.title.string) #<title>태그의 텍스트만 리턴
print(soup.title.get_text())#.string, .text(예전 버전)와 동일한 기능

#<body> 태그 접근
print(soup.title.parent)
print(soup.body)

# <h1> 태그 접근 : 동일한 태그가 여러 개 있을 경우 가장 먼저 나온 h1 태그를 출력.
print(soup.h1)
print(soup.h1.string)

# <a> 태그 접근 :
# 첫 번째 <a> 태그 요소 추출
print(soup.a)
print(soup.a.string) # <a> 태그 내부의 텍스트 추출(google)
print(soup.a['href']) # <a> 태그 내부의 href 속성의 url을 추출
print(soup.a.get('href')) # a['href']와 동일 기능.

#find('찾을 정보') 함수
print(soup.find('div')) # 해당 조건에 맞는 맨 처음 검색 결과를 추출

print(soup.find('div', {'id':'text_id2'}))
div_text = soup.find('div', {'id':'text_id2'})
print(div_text.text)

print(div_text.string)
href_link = soup.find('a', {'class': 'internal_link'})
href_link2 = soup.find('a', class_ = 'internal_link')

print(href_link)
print(href_link['href'])
print(href_link.get('href'))
print(href_link.text)
print('-')
print(href_link2)
print(href_link2['href'])
print(href_link2.get('href'))
print(href_link2.text)

print('href_link.attrs : ', href_link.attrs)
print('class 속성값 : ', href_link['class'])
print('values():', href_link.attrs.values())

values = list(href_link.attrs.values())
print('values[0]: {0}, values[1]: {1}'.format(values[0], values[1]))

href_value = soup.find('a', {'href': 'www.google.com'})
href_value2 = soup.find('a', attrs ={'href': 'www.google.com'})

print('href_value: ', href_value)
print(href_value['href'])
print(href_value.string)

print('-'*60)
span_tag = soup.find('span')
print('span tag:', span_tag)
print('attrs:', span_tag.attrs)
print('value:', span_tag.attrs['class'])
print('text:', span_tag.string)


print('-'*60)
print('* 모든 div 태그 검색 *')
soup = BeautifulSoup(html_example, 'html.parser')
div_tags = soup.find_all('div')
print('div_tags length: ', len(div_tags))

for div in div_tags :
    print('-'*30)
    print(div)

links = soup.find_all('a')
for alink in links:
    print(alink)
    print(f'url:{alink["href"]}, text:{alink.string}')
    print()

link_tags = soup.find_all('a', {'class':['external_link','interal_link']})
print(link_tags)

p_tags = soup.find_all('p', {'id':['first','third']})
for p in p_tags :
    print(p)

# <head> 태그 검색
soup = BeautifulSoup(html_example, 'html.parser')
head = soup.select_one('head')
print(head)
print('head.text:', head.text.strip())

# 첫 번째 <h1> 태그 검색
h1 = soup.select_one('h1')
print(h1)

# 클래스 이름 검색 : 태그.클래스 이름
class_link = soup.select_one('a.internal_link')
print(class_link)
print(class_link.string)
print(class_link['href'])

#계층적 하위 태그 접근 #1
#(상위태그>하위태그) 형식으로 접근 : 태그가 단계적으로 존재할 때
# link1 = soup.select_one('div#link > a.external_link')
# print(link1)
#
# link_find = soup.find('a', {'div' : 'link'})
# external_link = link_find.find('a', {'class' : 'external_link'})
# print('find external_link: ', external_link)

# 수정 코드.
link1 = soup.select_one('div#link > a.external_link')
print(link1)

link_find = soup.find('div', {'id':'link'})
external_link = link_find.find('a', {'class':'external_link'})
print('find_external_link: ', external_link)

# 계층적 하위 태그 접근 #2 : 공백으로 하위 태그 선언.
link2 = soup.select_one('div#class1 p#second')
print(link2)
print(link2.string)

# select() 함수
# 모든 <h1> 태그 검색
h1_all = soup.select('h1')
print('h1_all: ', h1_all)

# 모든 url 링크 검색.
print('-'*40)
url_links = soup.select('a')
for link in url_links:
    print(link['href'])

print('-'*40)
div_urls = soup.select('div#class1>a')

print(div_urls)
print(div_urls[0]['href'])

div_urls2 = soup.select('div#class1 a')
print(div_urls2)

# <h1 id = 'heading'>과 <h1 id = 'footer'> 항목 가져오기.
# 쉼표로 나열.
h1 = soup.select('#heading, #footer')
print(h1)

# <a>태그의 class 이름이 'external_link'와 'internal_link' 모두 검색.
url_links = soup.select('a.external_link, a.internal_link')
print(url_links)