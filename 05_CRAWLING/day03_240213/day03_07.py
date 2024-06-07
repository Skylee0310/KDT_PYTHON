from selenium import webdriver
from selenium.webdriver.common.by import By

agent_option = webdriver.ChromeOptions()
user_agent_string = 'Mozilla/5.0'
agent_option.add_argument('user-agent=' +user_agent_string)

driver = webdriver.Chrome(options=agent_option)
driver.get('http://nid.naver.com/nidlogin.login')
driver.implicitly_wait(5)

driver.find_element(By.NAME, 'id').send_keys('mila30717')
driver.find_element(By.NAME, 'pw').send_keys('@soyoka0830')

driver.find_element(By.ID, 'log.login').click()
# driver.quit()