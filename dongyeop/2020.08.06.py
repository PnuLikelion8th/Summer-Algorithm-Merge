

def solution(num):
    answer = 0
    
    while 1:
        if answer>=500:
            answer = -1
            break
        if num == 1:
            break
        if num%2 == 0:
            num=num/2
        else: num=num*3+1
        answer +=1
    return answer

    



print(solution(626331))
