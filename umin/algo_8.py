#핸드폰 번호 가리기
def solution(phone_number):
    phone_number = [int(i) for i in str(phone_number)]
    for i in range (0, len(phone_number)-4):
        phone_number[i] = '*'
    for i in range (-4, len(phone_number)):
        phone_number[i] = str(phone_number[i])
    answer = ''.join(phone_number)
    return (answer)

