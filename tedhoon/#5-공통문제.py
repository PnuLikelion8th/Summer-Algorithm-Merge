from bs4 import BeautifulSoup
from pprint import pprint
import requests
import re

def get_corona_patients():
    url = "http://www.busan.go.kr/covid19/Corona19.do"
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    req = requests.get(url, headers=headers)
    r = req.text

    soup = BeautifulSoup(r, "html.parser")
    
    table = soup.find_all('ul',tabindex="0")

    patient_num = 1
    for col in table:
        patient_info = col.select("li>span")
        print(f"{patient_num}) {patient_info[0].text} / {patient_info[1].text} / {patient_info[2].text} / {patient_info[3].text} / {patient_info[4].text} ")
        patient_num += 1

if __name__ == "__main__":
    get_corona_patients()

'''
1) 부산-205(연제구) / 접촉자 / 0 / 부산의료원 / 08/15 
2) 부산-204(연제구) / 접촉자 / 0 / 부산의료원 / 08/15 
3) 부산-203(사상구) / 해외입국 / 0 / 부산의료원 / 08/15
4) 부산-202(사하구) / 접촉자 / 0 / 부산의료원 / 08/15 
5) 부산-201(사하구) / 접촉자 / 0 / 부산의료원 / 08/15
.
.
.

참 쉽져 여러분
'''
