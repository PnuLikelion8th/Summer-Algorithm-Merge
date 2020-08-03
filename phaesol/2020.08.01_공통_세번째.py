
def solution(arr, divisor):

    result = []


    for i in arr:
        if i % divisor == 0:
            result.append(i)
        else:
            pass

    if result == []:
        result = [-1]


    return sorted(result)