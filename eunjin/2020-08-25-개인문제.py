# 크레인 인형뽑기 게임 - https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3

def solution(board, moves):
    basket = []
    size = len(board[0]) # NxN 크기의 N size
    count = 0
        
    for move in moves: # moves를 하나씩 실행
        for i in range(size):
            if board[i][move-1] != 0: # 인형이 있으면 
                if len(basket)>=1 and board[i][move-1] == basket[-1]: # 바구니 이전 인형과 같으면
                    basket.pop() # 삭제
                    count += 1
                else: # 다르면
                    basket.append(board[i][move-1]) # 바구니에 인형 넣기
                board[i][move-1] = 0 # 인형뽑기에서 인형 비우기
                break # 한 번 실행하면, for문 나가고 다음 move 실행하도록
                
    return count*2 # 사라진 인형 총 개수는 사라진횟수x2