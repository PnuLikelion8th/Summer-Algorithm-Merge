#콜라츠 추측
def solution(num):
    count = 0
    while  count <= 500: 
        if num == 1:
            return 0 
        if (num % 2 == 0): #if num == even number
            num = num/2 #divide with 2
            if num == 1:
                return count+1
            else : 
                count += 1
        elif (num % 2 != 0): #if num == odd number
            num = (num*3) + 1
            if num == 1:
                return count+1
            else : 
                count += 1
        if count == 500:
                count = -1
                break
    return count
