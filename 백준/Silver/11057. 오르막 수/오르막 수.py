# 2차원으로 문제를 푸는 경우
# N = int(input())

# arr = [ [0] * 10 for _ in range(N+1) ]
# arr[1] = [1] * 10
    
# for i in range(2, N+1):
#     for j in range(0, 10):
#         arr[i][j] = sum(arr[i-1][j:])


# print(sum(arr[N])%10007)

#N = int(input())

#dp = [1] * 10

#for i in range(2, N+1):
#    for j in range(10):
#        dp[j] = sum(dp[j:])
        
#print(sum(dp)%10007)        

N = int(input())

dp = [1] * 10

for _ in range(N-1):
    for j in range(1, 10):
        dp[j] += dp[j-1]
        
print(sum(dp)%10007)