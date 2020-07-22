def solution(n):
    i  = 0
    i_plus = 0
    for i in range(1,n+1):
        if n % i == 0:
            i_plus +=i
    return i_plus