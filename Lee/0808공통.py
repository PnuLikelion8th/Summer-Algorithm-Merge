# 콜라츠 추측
# num이 1이 될때까지 몇번이나 작업이 수행됬는지를 return해야한다
def solution(num):
    answer = 0
    while num!=1:
        if num%2 == 0:
            answer = answer+1
            # 작업을 한 번 할 때마다 answer에 1씩 더해준다 -> 얼만큼 수행됬는지 보려고!
            num = num/2
        else :
            answer = answer+1
            num = num*3+1

    if answer>=500:
        answer = -1
        # 작업이 500번 이상 수행됬다면 -1을 return

    return answer 
    
# 답은 나왔는데... 이렇게 하면 answer이 천 억 조가 되도 일단 값을 구한 다음 -1을  return 하고 만다
# while문 안에서 answer이 500이 되면 break를 걸고 싶은데 어떻게 적으면 좋을까 ?.?