import requests
from bs4 import BeautifulSoup

source = requests.get("http://www.busan.go.kr/covid19/Corona19.do").text
soup = BeautifulSoup(source, "html.parser")
hotKeys = soup.select("div.list_body")


for key in hotKeys:
    print(key.text)