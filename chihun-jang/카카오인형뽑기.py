# [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	[1,5,3,5,1,2,1,4]	4
# 입출력 예에 대한 설명

def solution(board, moves):
    answer = 0
    stack_box = [0]
    for i in moves:
        for sub_list in board:
            doll = sub_list[i-1]
            if doll !=0:
                
                if stack_box[-1] == doll:
                    stack_box.pop()
                    sub_list[i-1] = 0
                    answer += 2
                else:  
                    stack_box.append(doll)
                    sub_list[i-1] = 0
                break
        
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])