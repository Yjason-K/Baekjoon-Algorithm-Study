import sys
from collections import deque

di = [1, 0, -1, 0, 1, -1, 1, -1]
dj = [0, 1, 0, -1, -1, 1, 1, -1]


def bfs(i, j):
    q = deque()
    q.append((i, j))

    while q:
        ci, cj = q.popleft()
        for k in range(8):
            ni = ci + di[k]
            nj = cj + dj[k]

            if 0 <= nj < w and 0 <= ni < h and v[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni, nj))
                v[ni][nj] = 1


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        sys.exit()

    arr = []
    for _ in range(h):
        arr.append(list(map(int, input().split())))

    v = [[0] * w for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and v[i][j] == 0:
                v[i][j] = 1
                bfs(i, j)
                cnt += 1

    print(cnt)