def solution(n):
    pop_value_list = [v for v in range(1,n+1) if n%v==0]
    return sum(pop_value_list)
