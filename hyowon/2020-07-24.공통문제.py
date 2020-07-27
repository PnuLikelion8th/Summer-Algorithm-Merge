from string import ascii_lowercase,ascii_uppercase

def solution(s, n):
    list_s = list(s)
    lowerlist = list(ascii_lowercase * 2)
    upperlist = list(ascii_uppercase * 2)
    c = []
    for letter in list_s:
        if letter in lowerlist:
            a = lowerlist.index(letter)
            b = lowerlist[a+n]
        elif letter in upperlist:
            a = upperlist.index(letter)
            b = upperlist[a+n]
        else :
            b = letter
        c.append(b)
        str_c = ''.join(c)
    return(str_c)