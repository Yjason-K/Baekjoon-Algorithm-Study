def dfs(computers, visited, start):
    stack = [start]
    while stack:
        node = stack.pop()
        if visited[node] == 0:
            visited[node] = 1
            connected_nodes = [i for i, value in enumerate(computers[node]) if value == 1 and visited[i] == 0]
            stack.extend(connected_nodes)

def solution(n, computers):
    visited = [0] * n
    answer = 0
    for i in range(n):
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1
    return answer