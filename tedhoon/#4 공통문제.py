def solution(num):
    cnt = -1
    for _ in range(500):
        cnt += 1
        if num == 1:
            return cnt
        num = num//2 if num%2 == 0 else num*3+1 
    return -1
   
