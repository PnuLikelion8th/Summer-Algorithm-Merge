def convert_2(n,arr):
    arr_conv_2 = []
    for i in arr:
        tmp = ""
        for ex in range(n-1,-1,-1):
            if i//(2**ex) == 1:
                tmp += "1"
            else:
                tmp += "0"
            i = i%(2**ex)
            
        arr_conv_2.append(tmp)
    return arr_conv_2

def solution(n, arr1, arr2):
    answer = []
    arr1_bin = convert_2(n,arr1)
    arr2_bin = convert_2(n,arr2)
    for i in range(0,n):
        tmp_row = ""
        for j in range(0,n):
            if int(arr1_bin[i][j]) or int(arr2_bin[i][j]):
                tmp_row += "#"
            else:
                tmp_row += " "
        answer.append(tmp_row)
        
    return answer