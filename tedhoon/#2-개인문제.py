'''
https://programmers.co.kr/learn/courses/30/lessons/42747
programmers LV2 H-Index 문제
'''

def solution(citations):
    for i in range(max(citations), -1 , -1):
        cnt = 0
        for j in citations:
            if j >= i:
                cnt += 1
        if cnt == i:
            return cnt
        elif cnt > i:
            return i 
    return 0

'''
[브레인스토밍]

1편은 1회이상 인용되었나?
2편은 2회이상 인용되었나? 
3편은 3회이상 인용되었다? 
...

이런 생각의 흐름으로 check 후 맞을 시 True
근데 이걸 뒤부터 시작하면 효율이 좋을 것이다.(range를 뒤에서부터 돌린다.)

또한 예외 케이스로
[2,2,2] 경우 cnt는 3이 되지만 i가 3보다 작으면 3권이 3번 이상 이용된 게 아니다. 
더 나아가서, 2권이 2번 이상 당연히 인용되었을 것이므로 
cnt 가 i 보다 크다면
i 자신을 리턴한다.
'''

# test case
# print(solution([3, 0, 6, 1, 5]))
# print(solution([2,2,2]))
