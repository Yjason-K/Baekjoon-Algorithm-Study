def bfs(s, e):
    q = []
    v = [0] * (N+1)

    q.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)

        if c == e:
            return v[e] - 1

        for i in adj[c]:
            if v[i] == 0:
                q.append(i)
                v[i] = v[c] + 1
    return -1


N = int(input())
S, E = map(int, input().split())
M = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

ans = bfs(S, E)

print(ans)
