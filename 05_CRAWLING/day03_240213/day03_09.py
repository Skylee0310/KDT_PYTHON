from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://blog.naver.com.')
driver .switch_to_name*'mainFrame'

html = driver.page_source
soup = BeautifulSoup(html, html.parser)

whole_border = soup.find('div', {'id':'whole-border'})
results = whole_border.find_all('div', {'class''se-module'})
result1 = []
for result in results :
    print(result.text.replace('\n', ''))
    result1.append(result.text)