# DP 문제
# DP[i] = DP[i-2] * 2 + DP[i-1]
# DP[i-1] : 마지막 조각을 2x1 사각형으로 채운 방법의 수
# DP[i-2] : 마지막 조각을 2x2 사각형 또는 2x1 사각형 2개로 채운 방법의 수

n = int(input())
dp = [0] * (n+1)
dp[0] = dp[1] = 1

for i in range(2, n+1):
    dp[i] = 2*dp[i-2] + dp[i-1]
    
print((dp[n])%10007)