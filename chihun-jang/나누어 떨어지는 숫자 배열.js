function solution(arr, divisor) {
  var answer = [];
  arr.forEach((ele) => {
    if (ele % divisor === 0) {
      answer.push(ele);
    }
  });
  if (answer.length === 0) {
    return [-1];
  }
  return answer.sort((a, b) => a - b);
}
