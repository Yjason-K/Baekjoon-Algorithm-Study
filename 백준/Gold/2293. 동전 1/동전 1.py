import sys
input = sys.stdin.readline

def find_k():
    # dp 배열, k원을 만드는 경우
    dp = [0] * (k+1)
    dp[0] = 1 # # k원짜리 동전 하나로 k원을 만드는 경우의 수 = 1
    
    for coin in coins:
        for i in range(1, k+1): # i원인 경우
            if i - coin >= 0:
                dp[i] += dp[i - coin] # i - coin을 만드는 경우 더해주기
    return dp[k]

n, k = map(int, input().split()) # n가지 종류의 동전, 만들어야할 가치 k
coins = [ int(input()) for _ in range(n)] # 동전

print(find_k())
                
    