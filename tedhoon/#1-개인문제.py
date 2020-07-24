<<<<<<< HEAD
# https://programmers.co.kr/learn/courses/30/lessons/12915
# 프로그래머스 - 문자열 내 마음대로 정렬하기

def solution(strings, n):
    return sorted(sorted(strings), key=lambda x:x[n])

'''
풀고 줄이다 보니 1줄이 되긴했는데,
간단하게 밸류의 인덱스 기준으로 정렬은 sorted함수의 key를 이용하면 되었고,
key에서 익명함수 lambda를 써서 간단하게 인덱스에 해당하는 밸류만 뽑아냈음.
근데 2번 째 조건에서 "인덱스의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다." 라고 해서...
key값으로 sort하기 전에 미리 sorted를 한 번 먹여서 정렬해두면 쉽게 추가 조건을 만족하게 되었다능...
오늘도 날로먹은 것 같군 허허
'''
=======
# https://programmers.co.kr/learn/courses/30/lessons/12915
# 프로그래머스 - 문자열 내 마음대로 정렬하기

def solution(strings, n):
    return sorted(sorted(strings), key=lambda x:x[n])

'''
풀고 줄이다 보니 1줄이 되긴했는데,
간단하게 밸류의 인덱스 기준으로 정렬은 sorted함수의 key를 이용하면 되었고,
key에서 익명함수 lambda를 써서 간단하게 인덱스에 해당하는 밸류만 뽑아냈음.

근데 2번 째 조건에서 "인덱스의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다." 라고 해서...
key값으로 sort하기 전에 미리 sorted를 한 번 먹여서 정렬해두면 쉽게 추가 조건을 만족하게 되었다능...

오늘도 날로먹은 것 같군 허허
'''
>>>>>>> 8d4724011924eb9c2fd9fc4ecb058f7b1c22761c
