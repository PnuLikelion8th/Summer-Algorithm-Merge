package arimSeo;

//공통문제1) 이거슨 java췹스로 한 약수의 합....algorithmmmm

class Solution {
    public int solution(int n) {
        int sum = 0;
        
        for(int i=1; i<=3000; i++) { 
            if(n%i==0) {
                sum += i;
            }   //i배수가 n이면 합 계산(i는 n의 약수)
        }
            if(n==0) {  
                sum=0;
            }  //n=0 일때
        return sum;     
    }
}
