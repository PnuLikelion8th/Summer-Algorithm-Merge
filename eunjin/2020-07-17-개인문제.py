# 문자열 내림차순으로 배치하기

# Ver.1
def solution(s):
    for n in range(len(s)-1):
        for i in range(len(s)-1):
            if s[i] < s[i+1]:
                s = s[:i]+s[i+1]+s[i]+s[i+1+1:] # s[i+1]과 s[i] 자리를 서로 바꾸고 나머지는 그대로
    answer = s
    return answer

# Ver.2 - sorted를 몰랐었는데 '나누어 떨어지는 숫자 배열' 풀면서 알게돼서.. 간단하게 한 번 풀어봤습니당
def solution(s):
    return ''.join(sorted(s, reverse=True)) # sorted로 reverse=True하여(내림차순) 반환된 리스트를 -> join으로 문자열로 변경