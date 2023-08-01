from collections import deque

def bfs(x, y, h, visited):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] > h:
                queue.append((nx, ny))
                visited[nx][ny] = True

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_height = max(map(max, arr))

answer = 0
for i in range(max_height + 1):  # Iterate from 0 to max_height (inclusive)
    visited = [[False] * N for _ in range(N)]
    safe_zones = 0

    for j in range(N):
        for k in range(N):
            if not visited[j][k] and arr[j][k] > i:
                bfs(j, k, i, visited)
                safe_zones += 1

    answer = max(answer, safe_zones)

print(answer)
