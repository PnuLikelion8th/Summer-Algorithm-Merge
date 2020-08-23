def solution(d, budget):
    temp_sum = 0
    for i,v in enumerate(sorted(d)):
        temp_sum += v
        if temp_sum > budget: return i
    return len(d)

'''
아 뭐야
너무 간단한거네 이런
'''
