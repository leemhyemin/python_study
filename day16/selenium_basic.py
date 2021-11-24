# a나 buttor 찾기

# 셀레늄 : 웹 자동화 및 html  웹의 소스코드를 수집하는 모듈
from selenium import webdriver #셀레늄 모듈 로딩
import time as t
# 크롬 브라우저 자동으로 키는 법 물리드라이버 가동.
browser = webdriver.Chrome('D:/isec_Hmo3o/py_study/c_driver/chromedriver.exe')  #크롬 드라이버 깔린 경로

# 원하는 사이트로 이동
browser.get('https://www.naver.com')

# # 자동으로 메뉴나 링크 클릭 제어하기
# login_btn = browser.find_element_by_css_selector('#account> a')  #셀렉터 copy selector
# login_btn.click()

# 자동으로 텍스트 입력하기 (검색창에 검색어 입력)
search = browser.find_element_by_css_selector('#query')
search.send_keys('멍멍이')

t.sleep(2)

# search_btn = browser.find_element_by_css_selector(#search_btn)
search_btn = browser.find_element_by_xpath('//*[@id="search_btn"]')
search_btn.click()