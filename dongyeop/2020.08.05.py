
def solution(participant, completion):
    dictionary={}
    total = 0
    for i in participant:
        dictionary[hash(i)]= i
        total += hash(i)
    for j in completion:
        total -= hash(j)
    return dictionary[total]

print(solution(['leo','minsu','namin'],['minsu','namin']))

 def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]


print(solution(['alpha','minsu','namin','alpha'],['minsu','namin','alpha']))
