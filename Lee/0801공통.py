# 나누어 떨어지는 숫자 배열
# 숫자배열인 arr의 원소들 중 divisor로 나누어 떨어지는 녀석들을 담은 list를 return해야한다
# 나누어 떨어지는게 하나도 없으면 -1 return!
def solution(arr, divisor):
    answer = []
    # 일단 빈 리스트 만들고
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
             # i 원소들 중 divisor로 나누어 떨어지는 애들을 answer에 넣어준다
    if answer==[]:
        return [-1]
        # answer이 비어있으면 -1을 바로 return
    return sorted(answer)
    # 숫자 배열에 맞춰서 return해야 하므로 sorted!