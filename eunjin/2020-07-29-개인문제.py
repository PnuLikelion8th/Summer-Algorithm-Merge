# 2016년 - 2016년 1월 1일 금요일이면 2016년 a월 b일은 무슨 요일일까?

# - for문에서 range(1, a)가 아니라 (1, a)라고 그냥 쓰고 왜 안되지 이러고 있었다 ㅠㅠ
# - (1, a)는 그냥 튜플이라서 m에 1, a가 그대로 들어갔던거다.. 앞으로 실수 놉

def solution(a, b):
    day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'] # 일~토요일
    month29 = [2] # 29일까지 있는 월
    month30 = [4, 6, 9, 11] # 30일까지 있는 월
    month31 = [1, 3, 5, 7, 8, 10, 12] # 31일까지 있는 월
    count = 5 # 2016년1월1일은 금요일(day 리스트에서 index가 5)
    
    for m in range(1, a): # a월 이전까지 일수 모두 더하기 (1월~a-1월) -> a월1일로 만들기
        if m in month29:
            count += 29
        elif m in month30:
            count += 30
        elif m in month31:
            count += 31

    count += b-1 # b일까지 더하기 (1일~b일까지는 b-1번 더해야함)
    answer = day[count%7] # 7로 나눈 나머지 인덱스의 요일
    
    return answer