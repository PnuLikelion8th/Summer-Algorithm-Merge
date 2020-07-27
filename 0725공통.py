# 시저 암호.

def solution(s, n):
    l = "abcdefghijklmnopqrstuvwxyz"
    L = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # 일단 알파벳이 들어갈 문자열을 만든다
    answer = ""
    # 위에 answer을 안적어주면 for문이 돌때마다 초기화가 되서 맨 마지막 문자만 출력된다
    # 그리고 항상 "" <- 띄어쓰기를 조심하자
    for i in s:
        if i in l:
        # i 가 l 안에, 즉 소문자이면 
            if l.find(i) + n >= 26 :
            # 그런데 자릿값이 26을 넘어가버리면 알파벳 안에 없는거다
                answer += l[l.find(i) + n - 26]  
                # 그러니 26을 빼준다.
            else:
                answer += l[l.find(i) + n]
                # 안 넘어가면 그냥 써주면 되지 !

        elif i ==" ":
            # i가 공백이라면? -> 그냥 " "을 보내주면 된다
            answer += " "

        else:
            if L.find(i) + n >= 26 :
                answer += L[L.find(i) + n - 26]  
            else:
                answer += L[L.find(i) + n]

    return answer

