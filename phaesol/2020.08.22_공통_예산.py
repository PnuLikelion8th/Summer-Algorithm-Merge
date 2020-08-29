def solution(d, budget):
    num_list = []     
    a = sorted(d)      #최대한 많은 것들을 담아주기 위해 작은 것 부터 정렬
    if sum(d) <= budget: 
        return len(d)     # 만약 예산보다 지원 총금액의 합이 작거나 같으면, 그대로 리스트의 길이를 리턴
    else:
        for i in a:
            num_list.append(i)          # 총금액이 예산보다 크다면, for문을 통해 지원 금액을 작은 것부터 담아주다가 
            if sum(num_list) > budget:
                break                   # 예산보다 커지게 되면 함수 종료.
        return len(num_list)-1          # 커졌을 때 멈추므로 총길이에서 -1 해줌.