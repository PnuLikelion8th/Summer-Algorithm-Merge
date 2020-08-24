# 예산 - 최대한 많은 부서에 물품구매 지원할 때, 지원 부서의 수

def solution(d, budget):
    d.sort()
    
    cnt = 0
    for n in d:
        if budget >= n:
            budget -= n
            cnt += 1
        else:
            break
    return cnt