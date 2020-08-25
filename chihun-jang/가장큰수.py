def solution(numbers):
    sort_list = []
    cnt = 0
    for i in numbers:
        sort_list.append(((str(i)*4)[:4], cnt))
        cnt += 1

    answer = "".join([str(numbers[i[1]])
                      for i in sorted(sort_list, reverse=True)])

    if not int(answer):
        return "0"

    return answer
