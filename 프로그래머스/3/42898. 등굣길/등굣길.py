def solution(m, n, puddles):
    # 물에 잠긴 좌표 뒤집어 주기
    puddles = [[q,p] for [p,q] in puddles]
    dp = [[0] * (m + 1) for i in range(n + 1)]
    # 시작 지점
    dp[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 시작 지점은 건너뛰기
            if i == 1 and j == 1:
                continue
            # 웅덩이는 0으로 만들기
            if [i, j] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1])
    return dp[n][m] % 1000000007