import sys
input = sys.stdin.readline

def max_profit(D, T, P): # 퇴사까지 남은 날, 상담에 걸리는시간, 보수
    dp = [0] * (D+1)
    
    for i in range(D-1, -1, -1): #역순으로 계산
        if i + T[i] > D: # 상담이 퇴사 날짜를 넘기는경우
            dp[i] = dp[i+1] # 이전 날짜의 최대 수익을 그대로 가져옴
        else:
            dp[i] = max(dp[i+1], P[i] + dp[i + T[i]])
    return dp[0]

D = int(input())
T = []
P = []
for _ in range(D):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

print(max_profit(D, T, P))