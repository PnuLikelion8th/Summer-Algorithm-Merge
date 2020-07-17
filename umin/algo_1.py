def solution(n):
    answer = 0
    for i in range(1, 3000):
        if n % i == 0:
            answer += i
    return answer
