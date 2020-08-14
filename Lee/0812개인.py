# 모의고사
# 수포자 삼인방 중 시험에서 가장 높은 점수를 받은 사람을 return해야한다. 여러명이면 오름차순으로 !

def solution(answers):
    soopo_1 = [1, 2, 3, 4, 5]*2000
    soopo_2 = [2, 1, 2, 3, 2, 4, 2, 5]*1250
    soopo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000
    # 시험문제를 담은 answers는 최대 10000문제. 그러므로 각 수포자가 찍는 배열을 10000개로 맞춰준다.
    # out of range를 피하려고 이렇게 했는데.. 좋은 방법이 분명 있을 것 같다.

    soopo_1_score = 0
    soopo_2_score = 0
    soopo_3_score = 0
    # 수포자 삼인방의 점수. 밑의 함수로 맞출 때 마다 하나씩 올려줄 생각이다.

    for i in range(len(answers)) :
        if answers[i] == soopo_1[i]:
            soopo_1_score = soopo_1_score +1
        if answers[i] == soopo_2[i]:
            soopo_2_score = soopo_2_score +1
        if answers[i] == soopo_3[i]:
            soopo_3_score = soopo_3_score +1
    # answers의 i번째 인자와 각 수포자 답지의 i번째 인자를 비교! 맞으면 점수가 올라간다.

    all_score = [soopo_1_score, soopo_2_score, soopo_3_score]
    #  이 점수들을 몽땅 담은 all_score 리스트를 만든다. 왜냐? 제일 높은 점수를 구하기 위해 max를 쓰려고!

    who = []
    # 그런데 return값은 수포자 삼인방(1,2,3)중 제일 높은 점수의 사람을 담은 list여야 한다. 그래서 who 리스트도 만든다.

    for s in range(len(all_score)):
        if all_score[s] == max(all_score):
            # 마지막 관문. 1등이 여러명이면 얘네들을 이름순으로 담아줘야 한다.
            # all_score의 각 인자들을 최고점수인 max(all_score)과 비교!
            who.append(s+1)
            # max(all_score)과 같은 값의 인자들을 who에 담아준다. 0번째가 1이여야하니 +1 까지!
    return who