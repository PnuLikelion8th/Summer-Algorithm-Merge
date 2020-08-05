'''
프로그래머스 완주하지 못한 선수
'''


def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i,v in enumerate(participant):
        if i>=len(completion):
            return participant[-1]
        if v!=completion[i]:
            return v

'''
enumerate()를 이용하여 for문을 돌리게 되면
두가지 파라미터를 사용할 수 있게 되는데,
첫번 째로 index, 두번째로 해당 value를 사용할 수 있게됩니당

많이 애용하시라고 굳이 구구절절 써놓음

++ 동엽 진호 제출했길래 부랴부랴...
'''