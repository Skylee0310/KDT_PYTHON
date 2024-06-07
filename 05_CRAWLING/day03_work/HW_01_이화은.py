import urllib.request
import datetime
import json
from bs4 import BeautifulSoup
import requests
import collections
collections.Callable = collections.abc.Callable
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
함수 : print_rank_10
tbody > tr onmouseouver = "mouseOver(this)"에서 a 태그 내부의 class가 tltle 것 중 10개만 갖고 와야 함.
네이버 시가총액 페이지에서 찾고자 하는 항목의 페이지로 이동하여(webdriver 모듈 필요.) 해당 주식의 정보를 읽어와야 함. 

'''
def print_rank_10(url) :
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    # find_all 사용하여 내용 가져오기.
    fList = soup.find_all('tr', {'onmouseover':'mouseOver(this)'})
    # 교수님 코드 : tbody soup.find('tbody')
    #print(fListdd)
    print('='*100)

    while True :
        num = int(input('주가를 검색할 기업의 번호를 입력하세요(-1: 종료):'))
        if num == -1 :
            print('프로그램 종료')
            break
        elif 0<num<=10 :
            # 주식 항목 10개 추출
            print('[네이버 코스피 상위 10대 기업 목록]')
            nList = []
            urlList = []
            for fnc in fList[:10] :
                name = fnc.find('a', {'class':'tltle'})
                org_url = 'https://finance.naver.com/'
                add_url = name['href']
                srch_url = org_url+add_url
                nList.append(name.text)
                urlList.append(srch_url)
                #print(name) # 출력값 확인 용도.
                #print(srch_url) # 출력값 확인 용도.
            #print(nList) # 리스트에 요소가 추가되었는지 확인.
            #print(urlList) # 리스트에 요소가 추가되었는지 확인.

            # 출력 하기
            cnt = 1 # 숫자 인덱스 값 초기화.
            for f in nList :
                print(f'[{cnt:>2}] : {f}')
                cnt +=1
            srch_url = urlList[num-1]
            driver = webdriver.Chrome()
            driver.get(srch_url)
            print(srch_url)

            # 종목명 -> 입력 받은 숫자에서 -1 하여 인덱스로 입력.
            print('종목명 :', nList[num-1])

            # 종목 코드 -> div > span > class = code
            srch_code = driver.find_element(By.CLASS_NAME, 'code')
            print(srch_code.text) # 출력값 확인 용도.

            # 현재가, 전일가, 시가, 고가, 저가
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            price = soup.find('dl', {'class':'blind'}).text.split() #뒤늦게 알게 됨.

            print(f'현재가 : {price}')
            print(f'현재가 : {price[16]}')
            print(f'전일가 : {price[23]}')
            print(f'시가 : {price[25]}')
            print(f'고가 : {price[27]}')
            print(f'저가 : {price[31]}')

            driver.close()
            driver.quit()
            break
        else :
            print('입력 값이 잘못되었습니다.')

url = 'https://finance.naver.com/sise/sise_market_sum.naver'
print_rank_10(url)




# 시행 착오 ===> 50위인 아모레 퍼시픽까지 출력.
# for i in range(10) :
#     name = soup.find_all('a', {'class':'tltle'})
#     nList.append(name)
# print(nList)

# 시행 착오 2 ===> 각 주식 항목 링크 찾기, None 출력됨.
# find_a = fnc.find('td')
# srch_url = fnc.find(find_a.attrs['href'])