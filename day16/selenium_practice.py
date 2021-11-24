# 셀레늄 : 웹 자동화 및 html  웹의 소스코드를 수집하는 모듈
from selenium import webdriver #셀레늄 모듈 로딩
import time as t
# 크롬 브라우저 자동으로 키는 법 물리드라이버 가동.
browser = webdriver.Chrome('D:/isec_Hmo3o/py_study/c_driver/chromedriver.exe')  #크롬 드라이버 깔린 경로

# 원하는 사이트로 이동
browser.get('https://news.daum.net/society#1')
for m in range(1, 4):
    for n in range(1, 11):
        if m == 1:
            rank1 = browser.find_element_by_xpath(f'//*[@id="mAside"]/div[1]/ul/li[{m}]/div/ol[1]/li[{n}]/strong/a')
        else:
            rank1 = browser.find_element_by_xpath(f'//*[@id="mAside"]/div[1]/ul/li[{m}]/div/ol/li[{n}]/strong/a')
        rank1.click()
        t.sleep(1)
        # 1위 기사
        # rank1 = browser.find_element_by_css_selector(f'#mAside > div.aside_g.aside_ranking > ul > li.on > div > ol:nth-child(2) > li:nth-child({n}) > strong > a'





# mAside > div.aside_g.aside_ranking > ul > li.on > div > ol:nth-child(2) > li:nth-child(1) > strong > a
# mAside > div.aside_g.aside_ranking > ul > li.on > div > ol:nth-child(2) > li:nth-child(2) > strong > a
# #mAside > div.aside_g.aside_ranking > ul > li.on > div > ol:nth-child(2) > li:nth-child(3) > strong > a

# //*[@id="mAside"]/div[1]/ul/li[2]/div/ol/li[1]/strong/a
# //*[@id="mAside"]/div[1]/ul/li[3]/div/ol/li[1]/strong/a