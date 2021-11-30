from selenium import webdriver
from bs4 import BeautifulSoup
import time as t

# 날짜처리 라이브러리
from datetime import datetime

# 엑셀저장 라이브러리 
import xlsxwriter
# pip install xlsxwriter 다운로드

# 이미지 다운로드 처리 라이브러리
import urllib.request as req
from io import BytesIO



# 오늘 날짜 시간 
d = datetime.today()

# 파일명
file_name = f'교보문고 베스트 셀러_{d.year}_{d.month}_{d.day}.xlsx'

# 파일 저장 경로
file_save_path = f'D:/isec_Hmo3o/py_study/{file_name}'

# 엑셀라이브러리 객체 생성
workbook = xlsxwriter.Workbook(file_save_path)

# 엑셀 워크 시트 만들기
worksheet = workbook.add_worksheet()

# 행 꾸미기
styles = {
    'bold': True,
    'font_color': 'red',
    'bg_color': 'yellow'
}
cell_format = workbook.add_format(styles)


# 물리드라이버
browser = webdriver.Chrome('D:/isec_Hmo3o/py_study/c_driver/chromedriver.exe')

# 브라우저 원하는 사이즈로 키우기
browser.set_window_size(1280, 1080)

# 타겟 사이트로 이동
browser.get('http://www.kyobobook.co.kr/indexKor.laf?mallGb=KOR&orderClick=c1a')

######### 핵심 로직 ###########

# 국내도서 베스트셀러
t.sleep(2)
browser.find_element_by_css_selector('#bestSeller > div.section.on > div > div > a > img').click()


# 현재 페이지 소스코드 불러오기
html = browser.page_source

soup = BeautifulSoup(html, 'html.parser')

# 베스트 셀러 리스트 정보
best_list = soup.select('ul.list_type01 > li')

# print(f'{len(best_list)}개수: ')
# print(best_list[0])


for book in best_list:

    # 타이틀
    title = book.select_one('div.title').text.strip()
    # 저자
    # author_name = author.split('|')[0].strip()
    # main_authorm, sub_author = author_name_list
    author = book.select_one('div.author').text.strip()
    author_name_list = author.split('|')[0].split('저자 더보기')

    if len(author_name_list) == 1:
        main_authorm = author_name_list[0]
        sub_author = ''
    else:
        main_author, sub_author = author_name_list
    # 가격
    price = book.select_one('strong.book_price').text.strip()

    print(title)
    print(main_authorm.strip())
    print(sub_author.strip())
    print(price)

    print('=' * 70 )
  

