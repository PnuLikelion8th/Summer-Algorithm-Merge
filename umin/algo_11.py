#예산
def solution(d, budget):
    count = 0
    sum = 0
    d.sort()
    for i in range (len(d)):
        sum += d[i]
        if ( sum <= budget ) :
            count += 1
        elif ( sum > budget ) :
            break
    return(count)
