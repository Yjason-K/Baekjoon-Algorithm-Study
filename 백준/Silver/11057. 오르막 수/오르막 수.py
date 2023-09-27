N = int(input())

arr = [ [0] * 10 for _ in range(N+1) ]
arr[1] = [1] * 10
    
for i in range(2, N+1):
    for j in range(0, 10):
        arr[i][j] = sum(arr[i-1][j:])

print(sum(arr[N])%10007)