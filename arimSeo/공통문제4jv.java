//콜라츠 추측: https://programmers.co.kr/learn/courses/30/lessons/12943?language=python3

class Solution {
    public int solution(int num) {
        long n= num;
        int answer = 0;
        int i=0;

    for(; i<500 && n>1; i++) {
        if(n%2==0) {
            n= n/2;
        }
        else n= n*3+1;
    } 
    answer= (i==500) ? -1 : i;
    return answer;
    } 
}

// 자바의 삼항연산자 (i==500) ? -1 : i; 는 파이썬의 -1 if i==500 else i 와 같다