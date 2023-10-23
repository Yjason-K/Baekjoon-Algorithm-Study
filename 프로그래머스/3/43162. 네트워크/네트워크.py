from collections import deque

def bfs(computers, visited, start):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        
        # 방문하지 않은 경우만 처리
        if visited[node] == 0:
            # 방문으로 바꾸기
            visited[node] = 1
            for i, value in enumerate(computers[node]):
                # 연결된 컴퓨터이고 아직 방문하지 않았다면
                if value == 1 and visited[i] == 0:
                    queue.append(i)

def solution(n, computers):
    visited = [0] * n
    num_network = 0
    
    for i in range(n):
        if visited[i] == 0:
            bfs(computers, visited, i)
            num_network += 1
            
    return num_network
