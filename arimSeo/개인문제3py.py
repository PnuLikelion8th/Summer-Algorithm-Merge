# https://programmers.co.kr/learn/courses/30/lessons/12948
# 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

def solution(phone_number):
    return ('*'*(len(phone_number) -4)+ phone_number[-4:])



# 한줄이라니이있!!!!!한줄이라니ㅣ이ㅣㅣㅣㅣㅣㅣ 파이썬은 기적이다.....