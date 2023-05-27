def bfs(S, E):
    q = []
    v = [0] * 2000000

    q.append(S)
    v[S] = 1

    while q:
        c = q.pop(0)

        if c == E:
            return v[E] - 1

        for i in (c-1, c+1, c*2):
            n = i
            if 0<= n <= 200000 and v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1
    return -1  # 값이 잘못된 경우


S, E = map(int, input().split())
ans = bfs(S, E)
print(ans)