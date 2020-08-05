# programmers Lv.1 문자열 내 마음대로 정렬하기
# 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬
# 인덱스 n의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치

def solution(strings, n):
    a = []
    b = []
    for i in strings :
        i = i[:0] + i[n] + i[0:] # n번 인덱스를 첫번째기준으로 정렬하고 싶어서 제일 앞에 n번 인덱스를 추가
        a.append(i)
    a.sort() # 오름차순으로 정렬
    for i in a :
        i = i[1:] # 추가해준 글자를 다시 제외하여 
        b.append(i) # 새로운 리스트에 담아줌
    return b