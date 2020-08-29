# https://programmers.co.kr/learn/courses/30/lessons/42889
'''
카카오-실패율

딕셔너리 잘 안쓰게 되는 것 같아 이를 이용해서 풀어보았습니다..ㅎㅎㅎ
풀고 잘랬는데 눈떠보니 아침이군요
코드 리팩토링 따윈없습니다.. 출근 OMG...
'''

def solution(N, stages):
    answer = []
    
    pass_dic = {stage:0 for stage in range(1, N+2)}
    fail_dic = {stage:0 for stage in range(1, N+2)}
    result_dic = {stage:0 for stage in range(1, N+2)}

    for man in stages:
        for i in range(1, man+1):
            pass_dic[i] += 1
        fail_dic[man] += 1

    for k,v in pass_dic.items():  
        if v: result_dic[k] = fail_dic[k]/v
    
    del result_dic[N+1]
    
    for ans in sorted(result_dic.items(), key=(lambda x:x[1]), reverse=True):
        answer.append(ans[0])

    return answer

solution(5,[2, 1, 2, 6, 2, 4, 3, 3])
solution(4,[4,4,4,4,4])