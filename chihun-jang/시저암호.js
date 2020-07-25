function solution(s, n) {
  var mydict =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy";
  var answer = "";

  for (var i = 0; i < s.length; i++) {
    if (s[i] === " ") {
      answer += " ";
    } else {
      answer += mydict[mydict.indexOf(s[i]) + n];
    }
  }

  return answer;
}
