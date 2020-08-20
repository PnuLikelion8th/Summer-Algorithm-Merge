# programmers Lv.1 두 정수 사이의 합
# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴, a와 b의 대소관계는 정해져있지 않음

def solution(a, b):
    aftersort = sorted([a,b]) 
    # a,b의 대소관계가 정해져 있지 않아서 작은 수가 앞에 오도록 정렬
    answer = sum(range(aftersort[0], aftersort[1]+1))
    return answer
