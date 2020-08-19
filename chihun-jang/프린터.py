def solution(p, lo):
    flag = p[lo]
    cnt = 1

    if p.count(flag) != 1:
        p[lo] = 0

    while True:
        max_v = max(p)

        if max_v == flag:
            if p.count(flag) == 1 and not p.count(0):
                return cnt
            for i in p:

                if i == 0:
                    return cnt

                if i == flag:
                    cnt += 1

        for i in range(len(p)):

            if p[i] == max_v:
                p = p[i+1:]
                cnt += 1
                break
            else:
                p.append(p[i])


print(solution([9, 9, 9, 9, 9], 3))
