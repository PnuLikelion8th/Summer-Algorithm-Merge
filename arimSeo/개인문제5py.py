# 문자열다루기 기본: https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    answer = True

    for i in range(len(s)):
        if(len(s)==4 or len(s)==6):
            if(s[i] <'0' or s[i] >'9'):
                answer= False
        else: answer= False
    return answer



#다른 기똥찬풀이 발견! isdigit() 함수 이용하기
# def solution(s):
#     return s.isdigit() and len(s) in (4, 6)
# isdigit() : 숫자인지 아닌지 판별해줌.