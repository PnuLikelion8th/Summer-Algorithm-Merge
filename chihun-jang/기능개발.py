# Queue 자료구조를 사용해볼까 고민도 했지만 그렇게 효율이 좋을 것 같지 않아서 사용하지 않았습니다
def solution(arr1, arr2):
    answer = list()
    rev_prog = list(reversed(arr1))
    rev_speed = list(reversed(arr2)) #sorted의 평균 time compl는 nlogn이다.
    
    while rev_prog:
        for i in range(len(rev_prog)):
            rev_prog[i] += rev_speed[i]

        cnt = 0 
        while rev_prog[-1] >= 100:
            rev_prog.pop()
            cnt += 1
            
            if not rev_prog:
                break
                
        if cnt != 0:
            answer.append(cnt)
            
    return answer