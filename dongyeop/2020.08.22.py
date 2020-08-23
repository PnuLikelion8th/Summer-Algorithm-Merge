

def Solution(d,budget):
    d.sort()
    answer=0
    for i in d:
        if budget < i:
            break
        else: budget -= i
        answer += 1
    return answer
print(Solution([300,5300,4000,500,300], 6000))

