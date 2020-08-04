#가운데 숫자 리턴하기
def solution(s):
    n=len(s)/2
    answer=""
    if len(s)%2 != 0:

        answer += s[int(n)]  # 홀수면 가운데숫자를 리턴하고,
    else:
        answer +=s[int(n-1):int(n+1)]  # 짝수면 가운데 2글자를 리턴하라.

    return answer
