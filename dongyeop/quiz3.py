#문자열내 p와 q개수 세기

from collections import Counter

def solution(s):
    count = Counter(s.upper())
    if count['P']==count['Y']:
        return 'True'
    else: 
        return 'false'


print(solution('ogougijgjg'))