
#자연수 뒤집어 배열로 만들기
def solution(n):
    answer =list(reversed(tuple(str(n))))
    return list(map(int,answer)
