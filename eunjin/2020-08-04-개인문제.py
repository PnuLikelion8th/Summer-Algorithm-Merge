# 수박수박수박수박수박수? - 길이 n까지 수박 문자열 반복
# - // 연산자 : 나누기 후 소숫점 이하 버리고 정수 부분만 

# Ver.1
def solution(n):
    answer = ''
    subak = '수박'
    for idx in range(n):
        answer += subak[idx%2] # 짝수일 경우 '수', 홀수일 경우 '박' 뽑아와서 붙이기
    return answer

# Ver.2
def solution(n):
    return ('수박'*((n//2)+(n%2)))[:n] # (n//2)+(n%2) 길이로 늘린 후 n까지 자르기
    # return ('수박'*n)[:n] 도 가능하지만, n이 매우 큰 수라면 버려지는 것이 많으므로(효율성 문제) (n//2)+(n%2)만큼 늘리기