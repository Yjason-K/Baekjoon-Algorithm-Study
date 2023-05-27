def bfs(l, si, sj, ei, ej):
    q = []
    v = [[0] * l for _ in range(l)]
    
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)

        if ci == ei and cj == ej:
            return v[ci][cj] - 1

        for di, dj in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < l and 0 <= nj < l and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1

    return -1


n = int(input())

for _ in range(n):
    l = int(input())
    arr = [[0] * l for _ in range(l)]
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())
    print(bfs(l, si, sj, ei, ej))