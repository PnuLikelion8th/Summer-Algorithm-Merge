# 콜라츠 추측: https://programmers.co.kr/learn/courses/30/lessons/12943?language=python3

def solution(n):
    answer = 0

    while answer<500 and n>1:
        if n%2==0:
            n= n/2
        else: n= n*3+1
        answer+=1

        if answer==500:
            answer= -1
            break       #500번 반복할 경우 -1 반환하고 break로 나가기
    return answer



# 파이썬은 &&랑 ||가 없다! -> and랑 or로 적기
# 헉,,, 파이썬은 ++, --도 없었다!!