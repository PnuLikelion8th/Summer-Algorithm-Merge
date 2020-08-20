# 부산 꼬로나19 크롤링을 해부쟈아!~~
# pip install requests, pip install bs4, pip install lxml

import requests
from bs4 import BeautifulSoup

url = "http://www.busan.go.kr/covid19/Corona19.do"
res = requests.get(url)
res.raise_for_status()      #문제가 있으면 프로그램 바로 종료하도록(정상: 200)
soup = BeautifulSoup(res.text, 'lxml')

i=1
shape= soup.select('#contents > div > div.corona_list > div.list_body > ul')
for covid19 in shape:
    covid= covid19.select("li > span")
    print("["+str(i)+"]"+ f"{covid[0].get_text()}/{covid[1].get_text()}/{covid[2].get_text()}/{covid[3].get_text()}/{covid[4].get_text()}")
    i+=1
    
    
#  찾고 싶은 tag를 찾을 때는 find와 find_all을 사용
# 인덱스를 5번에 한번만 나오게/ 한줄로 정보/ 짝대기로 구별
