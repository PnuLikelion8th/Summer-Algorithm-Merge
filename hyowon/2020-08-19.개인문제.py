# programmers Lv.1 짝수와 홀수
# 정수 num이 짝수일 경우 Even을 반환하고 홀수인 경우 Odd를 반환

def solution(num):
    # if num % 2 == 0 :
    #     answer = 'Even'
    # else :
    #     answer = 'Odd'
    answer = "Even" if num%2 == 0 else "Odd"    
    return answer
