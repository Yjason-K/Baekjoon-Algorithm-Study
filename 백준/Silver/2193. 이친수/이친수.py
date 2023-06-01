def binary():
    dp = [0] * (n+1)
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]

    ans = dp[n]
    return dp[n]

n = int(input())
print(binary())