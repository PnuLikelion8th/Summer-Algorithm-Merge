# 웹 크롤링 - 네이버웹툰 인기순으로 가져오기
# enumerate() : 인덱스 번호와 원소를 tuple 형태로 반환 (idx, p)

import requests
from bs4 import BeautifulSoup

req = requests.get('https://comic.naver.com/webtoon/weekday.nhn?order=User')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
toon_lists = soup.select(
    'div.list_area.daily_all > div'
    )

day = "월화수목금토일"

for idx, toon in enumerate(toon_lists):
    print("------------------------------------{}요웹툰------------------------------------".format(day[idx]))
    cnt = 0
    while True:
        try:
            print(f"{toon.select('img')[cnt].get('title')} / ", end='') # 제목 가져오기
        except:
            break # 다음이 없으면 종료
        if cnt%5==4:
            print() # 5개마다 엔터
        cnt += 1
    print() # 엔터