from collections import deque
import sys
input = sys.stdin.readline

def bfs(visited, i, j):
    que = deque()
    que.append((i, j))
    visited[i][j] = 1

    while que:
        cur_i, cur_j = que.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = cur_i + di, cur_j + dj
            if 0 <= ni < N and 0 <= nj < M and cab_farm[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                que.append((ni, nj))

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    cab_farm = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    
    num_worms = 0
    
    for _ in range(K):
        x, y = map(int, input().split())
        cab_farm[y][x] = 1  # x는 열 인덱스, y는 행 인덱스
        
    for i in range(N):
        for j in range(M):
            if cab_farm[i][j] == 1 and visited[i][j] == 0:
                bfs(visited, i, j)  # bfs 호출 시 visited와 시작점 인덱스를 넘겨줍니다
                num_worms += 1
    
    print(num_worms)
