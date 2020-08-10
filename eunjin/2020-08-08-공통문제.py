# 콜라즈 추측 - 1로 만들기

def solution(num):
    count = 0
    while num!=1:
        if num%2==0: # 짝수면 2로 나누기
            num = num/2
        else: # 홀수면 3 곱하고 1 더하기 
            num = num*3 + 1
        count+=1
        if count==500: # 500번해도 1이 안 되면 -1 반환
            return -1
    return count