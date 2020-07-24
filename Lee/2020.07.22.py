#제일 작은 수 제거하기
#정수 배열 arr에서 가장 작은 수를 제거한 배열을 리턴해야 합니다
#리턴 배열이 비어있으면 -1을 리턴해야 합니다
def solution(arr):
    arr.remove(min(arr))
    # remove를 통해 arr안에 있는 인자를 제거할 수 있다
    # min을 통해 arr안에 있는 제일 작은 녀석을 찾을 수 있다
    # 이 둘을 합친다!
    if len(arr)==0:
        return(-1)
        # 그런데 arr이 비어있으면 -1을 리턴해야 한다
        # len()=0이 되면 안에 아무것도 없다는 뜻이니 if문을 써봤다
    else:
        return(arr)
        # 성공!

