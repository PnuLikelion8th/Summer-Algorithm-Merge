def solution(arr, divisor):
i = 0
while i<len(arr):
    if arr[i] % divisor != 0 :
        del arr[i]
    else :
        i+=1
if arr == []:
    return [-1]
arr.sort()
answer = arr
return answer
