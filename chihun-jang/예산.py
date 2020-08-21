def solution(d, budget):
    want_budget = 0
    cnt = 0

    for i in sorted(d):
        if want_budget + i > budget:
            break
        want_budget += i
        cnt += 1
    return cnt
