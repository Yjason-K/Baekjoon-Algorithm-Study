import sys
input = sys.stdin.readline


def maxScore():
    # dp테이블 생성 및 초기화
    dp = [[0] * 3 for _ in range(N+1)]
    for i in range(1, N+1):
        # 밟지 않는 경우
        dp[i][0] = max(dp[i-1][1], dp[i-1][2])
        # 1번 밟는 경우
        dp[i][1] = dp[i-1][0] + scores[i]
        # 2번 연속 밟는 경우
        dp[i][2] = dp[i-1][1] + scores[i]

    return max(dp[N][1], dp[N][2])


N = int(input())
scores = [0] + [int(input()) for _ in range(N)]

print(maxScore())

