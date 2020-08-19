#K번째수
def solution(array, commands):
    answer = []
    for i in range (len(commands)):
        temp_array = array[int(commands[i][0])-1:commands[i][1]]
        temp_array.sort()
        answer.append(temp_array[commands[i][2]-1])
    return answer
