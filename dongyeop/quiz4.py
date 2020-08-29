def solution(board, moves):
    stackbox = [] #뽑은거 쌓아올리는 리스트
    answer = 0
    for i in moves:
        for j in board:
            if j[i-1] == 0: 
                pass
            else:   #뽑았을 때
                stackbox.append(j[i-1])#뽑은거 스택박스에 넣어주고
                j[i-1] = 0#뽑았으니까 이전에 있던거에서 지워주고
                if len(stackbox) >=2 and stackbox[-1] == stackbox[-2]:#스택박스가 2개이상일때부터 맨뒤에꺼랑 그앞에꺼랑 같으면
                    del stackbox[-2:]#지워줌
                    answer += 2 #지워진 인형수 카운트해주고
                break #다음 뽑기로 이동

    return answer# ㅅㄱㅂㅇ~~~



print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))



    