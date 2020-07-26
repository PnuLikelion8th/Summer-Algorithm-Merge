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