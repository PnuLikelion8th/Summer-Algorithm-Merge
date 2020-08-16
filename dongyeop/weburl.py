import requests
from bs4 import BeautifulSoup
url ="http://www.busan.go.kr/covid19/Corona19.do"
webpage = requests.get(url)
html = webpage.text
soup = BeautifulSoup(html,'lxml')
result= soup.select('.list_body ul')

index = 0
for i in  result:
    index +=1
    print(str([index])+i.select('span')[0].get_text()+"/"+i.select('span')[1].get_text()+"/"+i.select('span')[2].get_text()+"/"+
    i.select('span')[3].get_text()+i.select('span')[4].get_text())
