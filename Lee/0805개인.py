# 완주하지 못한 선수
# 참가자 리스트 participant에서 완주자 리스트 completion에 없는 녀석을 return해야한다

def solution(participant, completion):
    run = sorted(participant)
    win = sorted(completion)
    # 우선 참가자와 완주자 리스트를 알파벳 순으로 정렬한다.

    # win.append("X")
    # => 완주자 리스트는 참여자보다 원소 하나가 모자라니 맨 뒤에 임의로 "X"를 넣었는데 없어도 잘 작동된다! 왜일까
    # 중복 없을 경우 맨 마지막 참여자가 정답이면 win[i]는 아예 존재 안하는데 이러면 왜 run[i]!=win[i]가 충족되는감??
    # 존재 하던 안하던 run[i]랑 다르니까 그냥 i를 return하는건가?.?

    for i in range(len(run)):
        # run과 win이 순서대로 주르르륵 배열되어있으니 0번부터 끝까지 하나씩 비교해주면 그만이다
        if run[i]!=win[i]:
            return run[i]
            # 비교하다가 i번째 원소가 다르면 그 run[i]를 return하면 끝!

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