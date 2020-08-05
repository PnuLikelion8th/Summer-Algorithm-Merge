// https://programmers.co.kr/learn/courses/30/lessons/12948
//전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

class Solution {
    public String solution(String s) {
        String answer = "";
        String s2= s.substring(0, s.length()-4);

        answer= "*".repeat(s2.length()) + s.substring(s.length()-4, s.length());
        return answer;
    }
}


 //for문 없이 java는 처음이라 몹싀 감격스럽습니더ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
 //뒤에4자리: s.substring(s.length()-4, s.length());