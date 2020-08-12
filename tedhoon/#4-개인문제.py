'''
프로그래머스 - 2019 카카오 개발자 겨울 인턴십 - 크레인 인형뽑기 게임
https://programmers.co.kr/learn/courses/30/lessons/64061
'''


def solution(board, moves):
    result_box = []
    cnt = 0
    for pop in moves:
        for single_line in board:
            if single_line[pop-1]:
                result_box.append(single_line[pop-1])
                single_line[pop-1] = 0
                if len(result_box) > 1:
                    if result_box[-1] == result_box[-2]:
                        del result_box[-2::]
                        cnt += 2
                break            
    return cnt

'''
아직도 변수명 지을때 고민이 된다..(잘 못지었다는 뜻..)
pop을 두번하는 것보다 del이 약간 성능이 좋았음

15라인에 if문을 지우고 싶었는데,
어차피 result_box에 담긴 인형과는 상관 없이 cnt만을 return하니까,
인형이 될 수 없는 1~100범주의 요소가 아닌 것을 하나 툭 넣어주면 15라인을 뺄 수 있겠다
'''
