# 문자열 내림차순으로 배치하기
def solution(s):
    for n in range(len(s)-1):
        for i in range(len(s)-1):
            if s[i] < s[i+1]:
                s = s[:i]+s[i+1]+s[i]+s[i+1+1:] # s[i+1]과 s[i] 자리를 서로 바꾸고 나머지는 그대로
    answer = s
    return answer