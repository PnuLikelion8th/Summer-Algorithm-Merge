def solution(numbers, hand):
    answer = ''
    cur_left = 10
    cur_right= 12
    change_zero = [11 if i == 0 else i for i in numbers]
    print(change_zero)
    for i in change_zero:
        if i % 3 == 1:
            cur_left = i
            answer += "L"
            
        elif i%3 == 0:   
            cur_right = i
            answer += "R"

        else:
            if (abs(cur_right-i)%3+abs(cur_right-i)//3) < (abs(cur_left-i)%3+abs(cur_left-i)//3):
                cur_right = i
                answer += "R"
            elif (abs(cur_right-i)%3+abs(cur_right-i)//3) > (abs(cur_left-i)%3+abs(cur_left-i)//3):
                cur_left = i
                answer += "L"
            else:
                if hand =="left":
                    cur_left = i
                    answer += "L"
                else:
                    cur_right = i
                    answer += "R"
        print("cur_left : ",cur_left, "cur_right : ", cur_right)
        print(answer)
    return answer