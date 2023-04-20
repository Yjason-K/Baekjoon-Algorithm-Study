n = int(input())

price = [0] + list(map(int, input().split()))

dp = [0] + [10e9] * n

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], dp[i-j] + price[j])
        
print(dp[n])