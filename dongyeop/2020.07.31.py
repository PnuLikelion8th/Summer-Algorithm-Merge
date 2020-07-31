def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i]%divisor==0:  #인덱스 번호로 접근
            
            answer+=[arr[i]]
            answer.sort()
    
    if all(i%divisor != 0 for i in arr):
        answer+=[-1]
    return answer

print(solution([1,10,3,5,79,60],5))

def solution2(arr, divisor):
    answer = []
    for i in arr:#요소에 바로 접근
        if i%divisor==0:  
            
            answer+=[i]
            answer.sort()#정렬
    
    if all(i%divisor != 0 for i in arr):#모든 i의 나머지가 0이 아니면
        answer+=[-1]#-1넣어준다
    return answer

    #맞나유??