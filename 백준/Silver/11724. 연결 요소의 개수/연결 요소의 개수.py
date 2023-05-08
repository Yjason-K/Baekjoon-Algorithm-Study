# 파이썬 재귀 제한 설정
import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

# 입력 설정
n, m  = map(int, input().split())

# empty graph 설정
graph = [ [] for _ in range(n+1)]

# 초기 visited 설정
visited = [False] * (n+1)

# dfs 재귀로 구현
def dfs(i):
    visited[i] = True
    for j in graph[i]:
        if not visited[j]:
            dfs(j)

# graph 입력 받기
for m in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
            
# 정답 값 초기화
count = 0

for k in range(1, n+1):
    if not visited[k]:
        count +=1
        dfs(k)
        
print(count)