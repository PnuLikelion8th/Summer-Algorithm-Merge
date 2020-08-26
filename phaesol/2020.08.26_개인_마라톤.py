#완주하지 못한 마라톤 선수

#효율성에 지지 마세요... 그냥 정답이면 정답이라 해죠..


#효율성 다 망한 코드 for에다가 if 에다가 count에다가 그래서 망한듯 그래도 정답이라 해줘


# def solution(participant, completion):
#     answer = ""
#     for i in participant:
#         if participant.count(i)>completion.count(i):
#             answer += i
#             break
            
#     return answer


def solution(participant, completion):

        p =  sorted(participant)           #문자도 잘 정렬이 되네여 그래서 정렬먼저해줌

        c =  sorted (completion)
        arr = p[1:len(p)-1]            # 나중에 else에서 쓸건데 첫과 끝 사이 값 리턴할거임. 
        arr_1 = c[1:len(c)]            #completion의 숫자가 한명이 작으니 len에다가 1 안빼야함.
                                        


  
        if p[-1] != c[-1]:                # 정렬했을 때 마지막을 비교해서 안맞으면 그 마지막이 완주자 리스트에는 없는 완주못한 선수니 리턴

            return p[-1]

        elif p[0] != c[0]:                
            return p[0]                  # 마찬가지로 첫번째 값이 안맞다 그러면 첫번째 선수가 완주못한거니 리턴


        elif  len(c) == 0:               # 참여자가 한명이고 완주자가 한명도 없을 경우도 있으니 이 경우 추가
            return p[0]                  
                                        
        else:
            for i in range(len(arr)):    # 문제는 이 곳. 첫 번째랑 마지막이 같다? -동명이인이 있다~

                if arr[i] != arr_1[i]:   # 그래서 사이에 있는 값을 for문으로 차례대로 비교해서 그 순서에 서로 안맞는 값이 있다? 걔가 완주 못한거임.
                    return arr[i]

# 설명이 이상해도.. 지금 약간 정신나가서 이상하면 피드백 해주세용 감사합니다 막차타게씀다.