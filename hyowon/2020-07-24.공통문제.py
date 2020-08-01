#list안해도됨(for문에서 순회하면서 하나씩 비교, str도 for문 순회) > 형변형과정(str>list>str)도필요x

from string import ascii_lowercase,ascii_uppercase

def solution(s, n):
    c = ''
    for letter in s:
        if letter in ascii_lowercase:
            a = ascii_lowercase.index(letter)
            b = (ascii_lowercase*2)[a+n]
            answer += b
        elif letter in ascii_uppercase:
            a = ascii_uppercase.index(letter)
            b = (ascii_uppercaset*2)[a+n]
            answer += b
        else :
            b = letter
            answer += b
    return answer

# def solurion(s, n):
#     list_s = list(s)
#     lowerlist = list(ascii_lowercase * 2)
#     upperlist = list(ascii_uppercase * 2)
#     c = []
#     for letter in list_s:
#         if letter in lowerlist:
#             a = lowerlist.index(letter)
#             b = lowerlist[a+n]
#         elif letter in upperlist:
#             a = upperlist.index(letter)
#             b = upperlist[a+n]
#         else :
#             b = letter
#         c.append(b)
#         str_c = ''.join(c)
#     return(str_c)
