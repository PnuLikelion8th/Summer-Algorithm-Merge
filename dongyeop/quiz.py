def solution(s,n):
    answer= ''
    alphabet_big="ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    alphabet_small=alphabet_big.lower()
   
    for i in range(len(s)):
        if s[i] in alphabet_big:
            index = alphabet_big.find(s[i])
            change = (index+n)%26
            answer+= alphabet_big[change]
            
        if s[i] in alphabet_small:
            index = alphabet_small.find(s[i])
            change = (index+n)%26
            answer+= alphabet_small[change]
        if s[i]==' ':
            answer+=' '
    return answer
print(solution('a sadsadB z	',4))