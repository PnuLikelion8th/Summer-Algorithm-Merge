# kakao 키패드 누르기: https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    ans =''
    L,R = 10,12         #시작위치 *(왼손)=10, #(오른손)=12

    for i in numbers:
        i=11 if i==0 else i     #키패드0: 11로 저장

# 키패드좌표 : 1줄에 번호3개
# 1:(0,0), 2:(0,1), 3:(0,2)....
        x,y=(i-1)//3, (i-1)%3           # 초기 키패드 숫자의 각 좌표(x:행끼리 같은 값, y:열끼리 같은 값)
        lx,ly = (L-1)//3, (L-1)%3       #다음 왼손 좌표
        rx,ry =(R-1)//3, (R-1)%3        #다음 오른손 좌표
        L_distance= abs(x-lx)+ abs(y-ly)        #가운데수 좌표와 왼손 사이 거리
        R_distance= abs(x-rx)+ abs(y-ry)        #      ""       오른손 사이 거리

        if i in [1,4,7]:
            ans+="L"
            L=i
        elif i in [3,6,9]:
            ans+="R"
            R=i              
        else:                               #키패드의 가운데 수 일때,
            if R_distance < L_distance:          #오른손에 가까우면
                ans+="R"
                R=i
            elif R_distance > L_distance:        #왼손에 가까우면
                ans+="L"
                L=i
            else:           #양손 거리 같으면,
                if hand=="right":      #오른손잡이는
                    ans+="R"      
                    R=i
                else:                  #왼손잡이는
                    ans+="L" 
                    L=i
    return ans



# keypad=[[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]

# 두 점사이의 거리 이용
# 가운데 숫자 칠때는 가까운 쪽 손가락 사용
# 상하좌우 4가지 방향으로만 이동(대각선 경우 x)
#파이썬은 자바 contains함수 x -> if _ in list이름

