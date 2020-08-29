# programmers Lv.1 모의고사
# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return

def solution(answers) :
    scores = [0, 0, 0] 
    answer = []
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3.3,1,1,2,2,4,4,5,5]

    for i in range(len(answers)):
        if answers[i] == pattern1[i % len(pattern1)]:
            scores[0] += 1
        if answers[i] == pattern2[i % len(pattern2)]:
            scores[1] += 1
        if answers[i] == pattern3[i  % len(pattern3)]:
            scores[2] += 1
    # for i in range(3):
    #     if max(scores) == scores[i] :
    #         answer.append(i + 1)
    answer = [i+1 for i in range(3) if max(scores) == scores[i]]
    return(answer)