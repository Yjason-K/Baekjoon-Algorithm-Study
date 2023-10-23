from collections import deque

def bfs(computers, visited, start):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if visited[node] == 0:
            visited[node] = 1
            for i, value in enumerate(computers[node]):
                if value == 1 and visited[i] == 0:
                    queue.append(i)

def solution(n, computers):
    visited = [0] * n
    answer = 0
    for i in range(n):
        if visited[i] == 0:
            bfs(computers, visited, i)
            answer += 1
    return answer