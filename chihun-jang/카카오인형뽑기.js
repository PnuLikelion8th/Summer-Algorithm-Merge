function solution(board, moves) {
  var answer = 0;
  var stack_box = [0];
  for (var i = 0; i < moves.length; i++) {
    for (var j = 0; j < board.length; j++) {
      var doll = board[j][moves[i]];
      if (doll !== 0) {
        if (stack_box[-1] === doll) {
          stack_box.pop();
          answer += 2;
        } else {
          stack_box.push(doll);
        }
        board[j][i] = 0;
        break;
      }
    }
  }
  return answer;
}

solution(
  [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1],
  ],
  [1, 5, 3, 5, 1, 2, 1, 4]
);

console.log(
  solution(
    [
      [0, 0, 0, 0, 0],
      [0, 0, 1, 0, 3],
      [0, 2, 5, 0, 1],
      [4, 2, 4, 4, 2],
      [3, 5, 1, 3, 1],
    ],
    [1, 5, 3, 5, 1, 2, 1, 4]
  )
);
