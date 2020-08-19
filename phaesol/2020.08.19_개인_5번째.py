def solution(array, commands):
    result=[]      
    for num in commands:
        i = num[0]-1
        j = num[1]         #i,j,k를 각각 내가 원하는 숫자로 정의해서 포문 돌림.
        k = num[2]-1
        array_list = sorted(array[i:j])    #슬라이싱한 리스트를 정렬해주고
        result_list = array_list[k]        #우리가 원하는 순서인 k번째 수 리턴해주고
        result.append(result_list)         # 그 숫자들을 리스트에다가 담아주기
    return result