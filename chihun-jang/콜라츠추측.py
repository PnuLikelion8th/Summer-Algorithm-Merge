
2
3
4
5
6
7
8
9
10
11
12
13
14
def solution(num):
    cnt = 0
    while True:
        if num ==1:
            return cnt
        elif cnt > 500:
            return -1
        elif num%2 == 0:
            cnt += 1
            num= num/2
        else:
            cnt += 1
            num = num*3 +1
