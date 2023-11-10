def dfs(i):
    visited[i] = 1
    n_i = permutation[i]
    if visited[n_i] == 0:
        dfs(n_i)
    return

T = int(input()) # 테스트 케이스 수
for _ in range(T):
    N = int(input())# 순열의 크기
    permutation = [0] + list(map(int, input().split())) # 순열
    visited = [0] * (N + 1) # 방문 여부 확인
    ans = 0
    
    for i in range(1, N + 1):
        if visited[i] == 0:
            dfs(i)
            ans += 1
            
    print(ans) # 존재하는 순열 사이클 찾기