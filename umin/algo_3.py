def solution(s, n):
    answer = ''
    a =[] #define list a 
    a = list(s) #문자열을 한 글자씩 끊어서 list a에 저장
    for i in range (len(a)):
        if( ord(a[i]) == 32 ) : #if blank
            a[i] = a[i]
        elif( 65 <= ord(a[i]) <= 90 ) :#if capital
            m = ord(a[i]) + n
            if ( m > 90 ):
                m -= 26
            a[i] = chr ( m )
        elif( 97 <= ord(a[i]) <= 122 ) : #if small
            m = ord(a[i]) + n
            if ( m > 122 ):
                m -= 26
            a[i] = chr(m)
    answer = ''.join(a)
    return answer
