def solution(s, n):
    mydic="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer =""
    for i in s:
        if i == " ":
            answer += i
        else:
            answer += mydic[mydic.find(i)+n]
    return answer