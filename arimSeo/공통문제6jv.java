// 예산 : https://programmers.co.kr/learn/courses/30/lessons/12982?language=java

class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        
    for(int i=0 ; i<d.length-1 ; i++){
        for(int j=0 ; j<d.length-i-1 ; j++){
            if(d[j] > d[j+1]){
                int bubble = d[j];
                d[j] = d[j+1];
                d[j+1] = bubble;
            }
        }
    }
    for(int i=0;i<d.length;i++){
        if(budget >= d[i]){
            budget-= d[i];
            answer++;
        }
    }
        return answer;
    }
}

//작은신청금액 부터 빼면서
//자바는 bubble sort로 굳이,,정렬 (자바도 Arrays.sort() 정렬메소드 쓰면 아주편리합니다^^)