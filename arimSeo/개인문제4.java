//두 정수사이합: https://programmers.co.kr/learn/courses/30/lessons/12912?language=java

class Solution {
    public long solution(int a, int b) {
        long ans =0;
        long answer = 0;
        int i;
        
        if(a< b) {
          for (i=a+1; i>a & i<b; i++) {
              ans += i;
              //=0+4=4, =4+5=9 
              answer= ans+a+b;
          } return answer;
        }
        elㅁ
   
        //또는 return b;
        
    }  
}