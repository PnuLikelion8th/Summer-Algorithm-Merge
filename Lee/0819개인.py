# 체육복
# 지금껏 이런 문제는 없었다 ... 라고 하기엔 끝내고 나니 너무나 간단 

def solution(n, lost, reserve):
    answer = n - len(lost)
    # 우선 전체 학생 수 n에서 체육복이 없는 사람 수인 len(lost)를 빼준다

    # --------------여기는 뻘짓-------------------
    # def overlap_L(L, R):
    #     temp_ans = 0
    #     for i in R : 
    #         if i in L :
    #             L.remove(i)
    #             temp_ans = temp_ans + 1
    #     return L, temp_ans
    # def overlap_R(L,R):
    #     for i in L : 
    #         if i in R :
    #             R.remove(i)
    #     return R
    # no_overlap_lost, temp_ans = overlap_L(lost, reserve) 
    # no_overlap_reserve = overlap_R(lost, reserve) 
    # ---------------------------------------------

    no_overlap_lost = list(set(lost)-set(reserve))
    no_overlap_reserve = list(set(reserve)-set(lost))
    temp_ans = len(lost+reserve) - len(set(lost + reserve))
    # 이 문제의 첫번째 핵심. 가장 먼저 lost와 reserve에 중복해서 있는 학생들을 빼줘야만 한다! 이게 가장 우선이다!!!
    # 그 과정에서 함수를 새로 만들어 for문으로 돌려 remove로 지우는 등의 엄청난! 뻘짓을 했다
    # 하지만 set함수를 쓰면 리스트 간 중복되는 녀석을 빼기란 너무나도 쉬운 일.
    # 덤으로 len(lost+reserve)-len(set(lost + reserve)) 이 녀석을 통해 중복되는 인자들의 개수를 알 수도 있다
    
    answer = answer + temp_ans
    # 중복된다 = 체육복이 있다 이므로 answer에다가 더해준다.

    for steel in no_overlap_lost:
        if steel - 1 in no_overlap_reserve :
            answer = answer + 1
            no_overlap_reserve.remove(steel - 1)

        elif steel + 1 in no_overlap_reserve :
            answer = answer + 1
            no_overlap_reserve.remove(steel + 1)

        # 이제 lost와 reserve간에 중복되는 인자가 없으므로 각 번호 양 옆에 여분이 있으면 빌려준다
        # 여기서 두번째 핵심. 학생2의 경우 1에게도 3에게도 빌릴 수 있는데, 학생4도 도난당했으면 2는 1에, 4는 3에 빌려야만 한다.
        # 그러므로 steel - 1부터 if문으로 돌려 자기보다 작은 번호 사람에게 우선적으로 빌리도록 만들어야 한다

    return answer


# 프로그래머스 실행을 돌려보면 처음에는 무조건 통과하는 테스트도 있고, 실패하는 테스트도 있다
# 그러면 실패하는 테스트를 찾아내서 뭐가 잘못인지를 알아야 하는데, 이것도 보통 일이 아니다
# hoxy나중에 풀고싶은 사람을 위해 실패 가능성이 아주 높은 테스트를 남긴다. 그럼 이만
# print(solution(5,[1,2,3],[2,3]))
# print(solution(5,[5,4,2],[2,4]))
# print(solution(5, [2,4], [1,3])) 
# print(solution(5,[4,5],[2,5]))



