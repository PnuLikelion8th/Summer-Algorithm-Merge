# 예산
# 부서국의 신청금액 d가 budget을 넘어가면 지원해줄수가 없다. 최대한 많은 부서를 지원해야!

def solution(d, budget):
    answer = 0
    d = sorted(d)
    # 최대한 많은 부서를 지원하기 위해서는? -> 작은 금액부터 예산을 분배해야 한다!
    # 그러므로 신청금액을 sorted !
    
    iwant = 0
    # 신청 금액의 총합을 iwant로 넣어줄 생각이다.

    for needs in d :
        iwant += needs
        # 신청금액 d의 인자들을 iwant에 하나하나 더해준다.
        
        if iwant > budget : 
            break
        # iwant가 budget을 넘어가면 지원해줄수가 없다. break !!

        answer = answer + 1
        # 넣을 때마다 지원된 부서 숫자는 하나씩 증가!
        # 단 break가 끝난 다음에 부서 숫자를 세야한다. 그 전에 세면 하나가 초과되니까! (이것땜에 한참 고생했다...)

    return answer