function solution(n) {
    var sum = 0
    for (var i = 1; i < n + 1; i++) {
        if (n % i === 0) {
            sum += i
        }
    }
    return sum
}