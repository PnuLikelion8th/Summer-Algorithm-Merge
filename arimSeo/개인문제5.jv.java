// 문자열다루기 기본: https://programmers.co.kr/learn/courses/30/lessons/12918
// 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.

class Solution {
    public boolean solution(String s) {
        boolean answer = false;     //@1
        int i= s.length();

        if(i==4 || i==6) {
            try{
                int a= Integer.parseInt(s);
                answer= true;
            }
            catch(Exception e){
                // answer= false; 없어도 ok
            }
        } return answer;
    }
}

// try-catch(예외문)는 쎄뚜쎗뚜~~ 예외처리할때 사용해요(이 문제에서는 문자열이 숫자로만 구성되어있는지 확인하기위해 사용함)
// try에서 예외가 발생하면 catch(예외문)로 넘어가는데, 그안에 실행할 내용이 없으면 처음 선언한 @1로 return해쥬요!
// int a= Integer.parseInt(s); 는 자바에서 string을 int로 형변환 시켜줍니다.

//자바 참 재미쬬~~?~???^!^

