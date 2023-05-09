import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False] * n
graph = [ [] for _ in range(n)] 
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)
    
def dfs(start, depth):
    if depth == 4:
        print(1)
        exit()
    next = graph[start]
    for i in next:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False

for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)