import requests
from bs4 import BeautifulSoup
source = requests.get("http://www.busan.go.kr/covid19/Corona19.do").text
soup = BeautifulSoup(source,"html.parser")
hotKeys= soup.select(".list_body ul")

index = 0
for key in hotKeys:
    index +=1
    print(str(index)+ ")" + key.select("li")[0].get_text() + "/" + key.select("li")[1].get_text() + "/" + 
    key.select("li")[2].get_text() + "/" + key.select("li")[3].get_text() + "/" + key.select("li")[4].get_text())