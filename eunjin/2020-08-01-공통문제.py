# 나누어 떨어지는 숫자 배열

# sort vs sorted : 정렬(오름차순), reverse=True일 경우 내림차순 정렬
# - lst.sort() : 리스트의 메소드로 "lst 자체를 변경"함.
# - sorted(lst) : 파이썬 내장함수로, lst를 변경한 결과룰 "리스트로 반환"함. 리스트 뿐만 아니라 어떠한 이터러블 객체도 가능

def solution(arr, divisor):
    answer = []
    for elem in arr:
        if elem%divisor == 0:
            answer.append(elem)
            
    if len(answer)==0: # 아무것도 없는 경우에 -1만
        answer.append(-1)
    else:
        answer.sort(reverse=False) # 오름차순 정렬
    return answer