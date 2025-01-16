function maxTriangleSum(n, triangle) {
    // DP 테이블 초기화
    const dp = Array.from({ length: n }, (_, i) => Array(triangle[i].length).fill(0));
    dp[0][0] = triangle[0][0]; // 초기값 설정

    // DP 점화식 적용
    for (let i = 1; i < n; i++) {
        for (let j = 0; j < triangle[i].length; j++) {
            if (j === 0) {
                // 왼쪽 경계
                dp[i][j] = dp[i - 1][j] + triangle[i][j];
            } else if (j === triangle[i].length - 1) {
                // 오른쪽 경계
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j];
            } else {
                // 가운데 값
                dp[i][j] = Math.max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j];
            }
        }
    }

    // 마지막 층에서 최대값 반환
    return Math.max(...dp[n - 1]);
}

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const inputN = Number(input[0]);
const inputLine = [];
for (let i = 1; i < input.length; i++) {
  inputLine.push(input[i].toString().trim().split(" ").map(v => Number(v)));
}

console.log(maxTriangleSum(inputN, inputLine))