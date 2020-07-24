#핸드폰번호 뒷자리 4개만 빼고 보이게하기 문제!
def solution(s):
    return '*'*(len(s)-4)+s[-4:]#척보면 척입니다.!