class Solution {
  public String solution(String s, int n) {
      String answer = "";
      int num = 0;
      for (int i = 0 ; i < s.length();i++){
          num = s.charAt(i);
          
          if (num == 32){
              num = num -n;
          }
          else if (num < 91){
              if(num+n >= 91){
                  num = num - 26;
              }
          }
          else{
              if(num+n>=123){
                  num = num-26;
              }
          }
          answer += Character.toString ((char) num+n);
      }
      return answer;
  }
}