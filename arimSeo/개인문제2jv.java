//문자열 내 p와 y의 개수: https://programmers.co.kr/learn/courses/30/lessons/12916
// 
// 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
// s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 
// 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

class Solution {
    boolean solution(String s) {
        String[] str= s.split("");
        int p_count=0; int y_count=0;

//p,y개수 count에 저장
        for(int i=0; i< str.length; i++) {
            if( str[i].contains("P") || str[i].contains("p")) {
                p_count++;
            }
            else if(str[i].contains("Y") || str[i].contains("y")) {
                y_count++;
            }
        }
       return p_count!= y_count ? false: true;
    } 
}
