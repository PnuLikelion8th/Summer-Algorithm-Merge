from string import ascii_uppercase, ascii_lowercase

def solution(s, n):
    result_temp_list = [] 
    input_value_list = s.split(' ') 
    for splited in input_value_list:
        result_temp = ''
        for i in splited:
            target_case = ascii_uppercase*2 if i.isupper() else ascii_lowercase*2
            result_temp += target_case[target_case.find(i) + n]
        result_temp_list.append(result_temp)
    return ' '.join(result_temp_list)

'''
대충.. 스플릿 두번해서
uppercase, lowercase 나누고,
각 글자를 순회하면서 묶음별로 모아서 append한다. 끝-

후기)
for문을 2번 쓰고싶진 않았지만
더이상 풀기가 싫다
왜냐하면 오늘은 금요일
금요일 좋아~
'''