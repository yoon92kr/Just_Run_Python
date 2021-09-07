# Selenium 외부모듈 다운 후 시행
# 웹드라이버에서 구현 할 코드

from selenium import webdriver
driver = webdriver.Chrome('./chromedriver.exe')

target_url = "http://www.naver.com/"

driver.get(target_url)

search_box = driver.find_element_by_name('query')

search_box.send_keys('Python')

search_box.submit()