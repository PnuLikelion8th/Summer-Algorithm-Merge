# 시저 암호

# Ver.1
from string import ascii_uppercase, ascii_lowercase

def solution(s, n):
    answer = ''
    for c in s:
        if c in ascii_uppercase: # 대문자이면
            lst = ascii_uppercase
            index = lst.index(c)+n # 시저암호로 변경한 index
            answer += lst[index % len(lst)] # 최대 index를 넘어가도 돌아오도록
        elif c in ascii_lowercase: # 소문자이면
            lst = ascii_lowercase
            index = lst.index(c)+n # 시저암호로 변경한 index
            answer += lst[index % len(lst)] # 최대 index를 넘어가도 돌아오도록
        else:
            answer += c

    return answer



# Ver.2 - 겹치는 부분을 간결화할 수 있을 것 같아서 수정해봤습니다
# str.find() vs index() : find는 값을 못 찾으면 -1 리턴, index는 ValueErorr
# - find() : str만 가능
# - index(찾을값, 시작인덱스, 종료인덱스) : str, list 둘 다 가능
from string import ascii_uppercase, ascii_lowercase

def solution(s, n):
    answer = ''
    for c in s:
        if c in ascii_uppercase: # 대문자이면
            lst = ascii_uppercase
        elif c in ascii_lowercase: # 소문자이면
            lst = ascii_lowercase
        else:
            answer += c
            continue
        index = lst.find(c)+n # 시저암호로 변경한 index
        answer += lst[index % len(lst)] # 최대 index를 넘어가도 돌아오도록

    return answer