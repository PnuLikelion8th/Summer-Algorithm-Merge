def solution(num):
    count = 1
    if num == 1:
        return 0   #1일 경우에는 카운트 0 리턴
    while num != 1:
        if num%2 != 0:
            num =  num*3+1    # 1이 아닌 경우 홀수, 짝수에 맞는 조건문 실행

        elif num%2 == 0:
            num = num/2

        if num == 1:
 
            return count      #1일 되면 그 숫자 리턴

        count= count+1

        if count >=500:
            return -1         # 500번 넘어가면 -1 리턴