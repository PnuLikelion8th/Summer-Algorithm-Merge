def solution(s,n):
    
    
   
    a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    A=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    #아스키 코드로 실행해보려 했으나 실패라서 노가다로 직접 적었습니다 ㅎ...
    
    result = '' # 최종 값을 리턴해줄 곳입니다.
    
        
    for i in s:           # 요소 하나하를 for문으로 빼줍니다.
        if i in a:        #큰 if문 - 소문자인지 , 대문자인지 구분/ 작은 if문 - i+n이 z를 넘어가지 않을 때와 넘을때를 구분
            if (a.index(i)+n<26) :
                
                result += a[a.index(i)+n] 
            else  :
                 
                result += a[a.index(i)+n-26] 
        elif i in A:
            if (A.index(i)+n<26) :
                
                result += A[A.index(i)+n]
            else :
                
                result += A[A.index(i)+n-26]
        else :
            result +=' '           #공백은 그대로 공백으로 돌려주기
   

    return result                  #위에 조건문들을 통과한 요소 하나하나를 result에 담아주기

print(solution('A F z',5))         # 실험해보기 위한 코드