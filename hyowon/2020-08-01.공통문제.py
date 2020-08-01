def solution(arr, divisor):
    a = []
    for i in arr : 
        if i % divisor == 0 :
            a.append(i)
            a.sort()
    if len(a) == 0 :
        a = [-1]
    return a