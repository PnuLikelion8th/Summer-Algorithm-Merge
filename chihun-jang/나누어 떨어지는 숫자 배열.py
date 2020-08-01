def solution(arr, divisor):
    answer = [i for i in arr if i%divisor==0]
    if len(answer) ==0:
        answer.append(-1)
    return sorted(answer)