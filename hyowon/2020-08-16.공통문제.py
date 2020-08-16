import requests
from bs4 import BeautifulSoup

url = 'http://www.busan.go.kr/covid19/Corona19.do'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

corona = soup.select('div.list_body > ul')


cnt = 0
for i in corona :
    cnt += 1
    print( str(cnt) + ') '+ i.select('span')[0].get_text() + " / " + i.select('span')[1].get_text() + " / " + i.select('span')[2].get_text() 
    + " / " + i.select('span')[3].get_text() + " / " + i.select('span')[4].get_text())