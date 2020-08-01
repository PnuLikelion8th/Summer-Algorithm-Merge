#  문자열 내 p와 y의 개수: https://programmers.co.kr/learn/courses/30/lessons/12916
# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
# s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 
# 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 
# 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

def solution(s):
    return False if s.lower().count("p")!= s.lower().count("y") else True

#sol) p개수, y개수 다르면 false/ 나머지 경우는 true



# 처음에 아래와 같이 했는데, 틀렸다고 나왔는데 파이썬에서는 이렇게 쓰면 뭐가 문제인지 궁금합니댜 고수님덜!!!
# def solution(s):
#   s.lower()
#   return False if count("p")!= count("y") else True
