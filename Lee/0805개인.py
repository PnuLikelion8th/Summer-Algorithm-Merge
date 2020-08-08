# 완주하지 못한 선수
# 참가자 리스트 participant에서 완주자 리스트 completion에 없는 녀석을 return해야한다

def solution(participant, completion):
    run = sorted(participant)
    win = sorted(completion)
    win.append("X")
    for i in range(len(run)):
        # run과 win이 순서대로 주르르륵 배열되어있으니 0번부터 끝까지 하나씩 비교해주면 그만이다
        if run[i]!=win[i]:
            return run[i]
            # 비교하다가 i번째 원소가 다르면 그 run[i]를 return하면 끝!

print(solution(["a","b","c","b"],["a","b","c"]))
# 밑에 적은 여러 뻘짓들은 답은 나오지만 효율성에서 빵점을 받는다.
# 특히 for문 돌린 remove나 count는 효율성이 굉장히 떨어지는걸로 친다. 컴퓨터 바보
# ----------------------------------------------------------------------------
# def solution(participant, completion):
#   for i in participant:
#     if i in completion:
#         completion.remove(i)
#     else:
#         answer = i
#   return answer

#    if len(set(run))==len(run):
#        for i in run:
#            if i not in win:
#                return i
#     else:
#        for i in run:
#            if participant.count(i)!=completion.count(i):
#                return i