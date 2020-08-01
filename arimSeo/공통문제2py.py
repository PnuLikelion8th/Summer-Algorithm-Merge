# 파이썬에서는 문자를 아스키코드를 나타내는 int형으로 변환하고 연산한 뒤 다시 char형으로 형변환 해주어야 한다.
    #예: c= chr(ord('s'))
    
def solution(s, n):
    result=""
    c= list(s)

#깔쌈하게 자바엔 안쓴 삼항연산자 함 써보ㄲ 했는데.. 몹씨 보기싫어짐 (if문 축약) 
    for i in range(0,len(c)):
        if ord(c[i]) >= ord('a') and ord(c[i])<= ord('z'):
            result += chr(ord(c[i])+n-26 if ord(c[i])+n > ord('z') else ord(c[i])+ n )
        elif ord(c[i]) >= ord('A') and ord(c[i])<= ord('Z'):
            result += chr(ord(c[i])+n-26 if ord(c[i]) +n > ord('Z') else ord(c[i])+ n ) 
        else:
            result += " "
            
    return result        
            