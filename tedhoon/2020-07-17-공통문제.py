def solution(n):
    pop_value_list = [v for v in range(1,n+1) if n%v==0] 
    answer = sum(pop_value_list)
    return answer