# 웹 크롤링 - 코로나 확진자 정보 가져와서 출력

import requests
from bs4 import BeautifulSoup

# HTTP GET request
req = requests.get('http://www.busan.go.kr/covid19/Corona19.do')
# HTML 소스 가져오기
html = req.text
# bs4 이용하여, html소스->python객체 변환
soup = BeautifulSoup(html, 'html.parser')
# select : CSS selector를 이용하여, 조건과 일치하는 모든 객체를 list로 반환
corona_lists = soup.select(
    'div.corona_list > div.list_body > ul > li > span' # 해당 부분 다 가져오기
 )

index = 0
for corona in corona_lists:
    # 중간에 '~~관련' 부분은 출력하지 않도록 (관련 글자가 포함돼있거나, 비어있으면 넘어가기)
    if corona.text=='' or '관련' in corona.text:
        continue
 
    end=' / '
    if index%5 == 0: # 확진자정보 하나의 첫 시작이면 '숫자)' 출력
        print(index//5+1,')', sep='', end=' ')
    elif index%5 == 4: # 확진자정보 하나가 끝나면 엔터로 넘어가기
        end='\n'
        
    print(corona.text, end=end)
    index+=1