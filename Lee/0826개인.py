# 카카오 1차 다트게임
# 이것이 1차라니... 개발자의 길은 멀고도 멀고도 험하다

def solution(dartResult):
    all_score = []
    # 일단 모든 점수들을 담을 list를 만든다
    original = ''
    # 아무 보너스를 받지 않은, 원래의 점수 !
    for i in dartResult:
        if i.isnumeric():
            original = i + original
        # isnumeric라는 신비한 함수를 알게 되었다. 덕분에 i가 숫자일 경우 -> original점수에 더한다!
        
        elif i == 'S':
            all_score.append(int(original) ** 1)
            original = ''
        elif i == 'D':
            all_score.append(int(original) ** 2)
            original = ''
        elif i == 'T':
            all_score.append(int(original) ** 3)
            original = ''
        # 다음으로는 영역 점수(S/D/T)를 계산. 각 영역에 해당되는 점수 제곱을 해준 후 all_score에 더하면 된다.
        # 점수 계산이 끝난 것이니 original은 다시 0으로!

        elif i == '*':
            if len(all_score) > 1:
                all_score[-2] = all_score[-2] * 2
            all_score[-1] *= 2
        #  대망의 옵션부분. *이 걸렸을 때는 해당 점수와 바로 앞 점수가 두배 / #은 해당점수 마이너스 이다.
        #  len(all_score)>1 이면 첫번째 기회가 아니라는 뜻! -> 바로 앞 점수도 두배로 해준다.

        elif i == '#':
            all_score[-1] = all_score[-1] * - 1
        # #일 경우에는? 해당 점수는 마이너스 값이 되게끔!

    return sum(all_score)