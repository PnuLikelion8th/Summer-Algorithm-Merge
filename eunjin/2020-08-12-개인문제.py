# 완주하지 못한 선수
# - 완주하지 못한 최은진 합류 😭😭
# 리스트->str : '연결되는부분'.join(리스트)

# Ver.1 - 효율성테스트 통과 못함 (50점)
def solution(participant, completion):
    for cmpl in completion:
        participant.remove(cmpl) # 싹다 삭제
    return ''.join(participant) # 남은걸 리턴
    
# Ver.2 - 이것도 효율성테스트 통과 못함 (50점)
    for part in participant:
        if part in completion:
            completion.remove(part) # 찾으면 삭제
        else:
            return part # 못찾으면 리턴

# 효율을 어떻게 하면 올릴 수 있을지.. 좀 더 고민해보겠습니다 ...안돼서 다른문제 풀었음 흑흑



# 문자열 다루기 기본
# - s가 4or6 and 숫자로만구성 확인

def solution(s):
    if len(s) != 4 and 6:
        return False
    
    numlst = '1234567890'
    for c in s:
        if c not in numlst:
            return False
    return True