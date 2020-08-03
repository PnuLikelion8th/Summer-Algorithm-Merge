def solution(arr, divisor):
        answer = []
        arr.sort()   # 오름차순으로 정렬

        for i in range(len(arr)):
            if arr[i]%divisor ==0:
                answer.append(arr[i])
        if len(answer)==0:
            answer= [-1]
        return answer