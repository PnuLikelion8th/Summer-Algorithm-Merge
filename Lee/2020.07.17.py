def solution(n):
    l = []
    #약수의 합->sum 함수를 쓰고 싶어서 빈 list를 만들었따.
    for a in range(1, n+1):
        #약수가 될 수 있는 a의 범위를 정했다. 약수니까 n보다 크면 안된다.
        if n % a ==0:
            l.append(a)
            #n을 a로 나눴을때 나머지가 0이면 바로 약수인 것이다. 그러한 a들을 list에 추가!
    answer = sum(l)
    #list에 모인 a를 몽땅 더하면 바로 답이 되는 것이다.


    # n = int(input("숫자"))
# l = [2]
# for k in range(1,n+1):
#     for a in range(2,k):
#         while a < k:
#             if k % a==0:
#                 pass
#             else:
#                 l.append(k)
# print(len(l))
# 소수 : 1과 자기 자신을 제외한 숫자로 나누면, 나머지가 생김
# 소수가 아닌 수 : 자기 자신을 제외한 숫자 중, 나머지가 0인 수가 있음