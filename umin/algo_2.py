//프로그래머스 코딩테스트 두 정수 사이의 합
def solution(a, b):
    answer = 0
    //두 정수 a, b에 대하여
    if (a<b)://a가 b보다 작은 경우
        for i in range (a,b+1):
            answer += i//a부터 b까지 더한 값을 answer에 저장 
    else://b가 a보다 크거나 같은 경우
        for i in range (b,a+1):
            answer += i
    return answer