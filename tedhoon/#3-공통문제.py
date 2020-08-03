def solution(arr, divisor):
    result = sorted([v for v in arr if v%divisor == 0])
    return result if result != [] else [-1]

'''
프로그래머스 - 나누어 떨어지는 배열
'''