def solution(n):
    answer =0

    for i in range(1,3001):
        if n%i==0:
            answer += i
    if n==0:
        answer =0
    return answer