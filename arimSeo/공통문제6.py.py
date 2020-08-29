#예산 : https://programmers.co.kr/learn/courses/30/lessons/12982?language=python3

# sort 함수 사용
def solution(d, budget):
    answer = 0
    summ=0
    d.sort()
    for i in range(len(d)):
        if d[i]+ summ<= budget:
            summ+=d[i]
            answer+=1

    return answer


# 신청금액d 합쳤을때 예산보다 big -> 예산에맞게 부서pick / small or same -> 모든부서 지원
# 최대한 많은 부서 지원해주도록/ 예산 안에서/ return 지원부서개수