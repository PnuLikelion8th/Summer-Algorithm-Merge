# programmers Lv.1 K번째 수
# [i, j, k]를 원소로 가진 배열 commands가 주어질 때 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 배열에 담아 return

def solution(array, commands):
    answer = []
    for c in commands : 
        # commands의 원소c로 부터 i,j,k값 구하기
        i = c[0] 
        j = c[1]
        k = c[2] 
        # a = array[i-1:j] : 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고
        # a.sort() : 정렬했을 때
        # b = a[k-1] : k번째에 있는 수를
        # answer.append(b) : 배열에 담음
        answer.append(sorted(array[i-1:j])[k-1]) # 위에 과정을 한 줄로 정리
    return answer