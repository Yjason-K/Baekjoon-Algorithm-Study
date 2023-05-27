from collections import deque

def bfs():
    q = deque()
    v = [[-1] * M for _ in range(N)]

    # 익지 않은 토마토 갯수 확인
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt += 1
            elif arr[i][j] == 1:
                q.append((i, j))
                v[i][j] = 0

    while q:
        ci, cj = q.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0 and v[ni][nj] == -1:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                cnt -= 1
        
    if cnt == 0:
        return max(map(max, v))
    else:
        return -1


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = bfs()
print(ans)
