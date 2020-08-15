from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_info():
    URL  = 'http://www.busan.go.kr/covid19/Corona19.do'
    html_tag = BeautifulSoup(urlopen(URL), 'html.parser')
    parsing_tag = html_tag.select('#contents > div > div.corona_list > div.list_body > ul')

    list_tag = [v for v in parsing_tag]

    cnt = 1
    display_txt =""
    for i in range(len(list_tag)):
        if list_tag[i].select('li > span')[2].text:
            tmp_list =list_tag[i].select('li > span')
            print( f'{cnt}) {tmp_list[0].text} / {tmp_list[1].text} / {tmp_list[2].text} / {tmp_list[3].text} / {tmp_list[4].text}')
            cnt += 1

get_info()