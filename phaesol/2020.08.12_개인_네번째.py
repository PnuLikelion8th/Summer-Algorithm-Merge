#문자열 역순으로 정렬하기
def solution(s):
    s_list = list(s)
    sort_list = sorted(s_list)  #여기서 정렬하고 바로 뒤집어줬으면
    upper=""
    lower=""
    for i in sort_list:
        if i.isupper():
            upper+= i
        else:
            lower += i
    answer = list(reversed(lower))+list(reversed(upper))      #이러한 귀찮은 과정이 없어도 된다는거..ㅠ
    return "".join(answer)