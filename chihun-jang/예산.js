function solution(d, budget) {
  var answer = 0;
  var want_budget = 0;
  d.sort((a, b) => a - b);
  d.map((item) => {
    want_budget += item;
    if (want_budget <= budget) {
      answer += 1;
    }
  });
  return answer;
}
