# 자동 로그인

from selenium import webdriver
driver = webdriver.Chrome('./chromedriver.exe') #사용할 익스플로러

target_url = "https://nid.naver.com/nidlogin.login" #호출할 페이지 url 대입

driver.get(target_url)  #웹 크롤링을 통한 페이지 url 가져오기

driver.find_element_by_name('id').send_keys('아이디')   # 로그인 창 찾기 + id 입력하기
driver.find_element_by_name('pw').send_keys('비밀번호') # 패스워드 창 찾기 + pw 입력하기

driver.find_element_by_class_name('btn_global').click() # 로그인 버튼 클릭