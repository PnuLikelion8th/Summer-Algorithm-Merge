// https://programmers.co.kr/learn/courses/30/lessons/12926?language=java 시저암호

class Solution {
    public String solution(String s, int n) {
        char[] array_s = s.toCharArray();       //배열로 마 만들어쁘림
        String result="";
    
        for(int i=0; i<array_s.length; i++) {
            char str= array_s[i];
            
            if(str>='a' && str<='z') {
                if(str + n > 'z') {                      //z넘어갈 경우 (z다음은 머다??? a가 된다~~)
                    result += (char) (str+n-26);         //알파벳 26가지
                }
                else result += (char) (str+n);
            }   
            else if(str >='A' && str<='Z') {
                if((str + n > 'Z')) {
                    result+= (char) (str+n-26); 
                 }
                else result+= (char) (str+n);
            }
            else
                result +=" ";           //이건 마 공백이다이
            
        }   return result;
    }  
}