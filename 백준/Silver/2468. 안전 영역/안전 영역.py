import sys
sys.setrecursionlimit(100000)

def dfs(x, y, h):
    if x < 0 or x >= N or y < 0 or y >= N or visited[x][y] or arr[x][y] <= h:
        return

    visited[x][y] = True
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        dfs(nx, ny, h)

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
                dfs(j, k, i)
                safe_zones += 1

    answer = max(answer, safe_zones)

print(answer)
