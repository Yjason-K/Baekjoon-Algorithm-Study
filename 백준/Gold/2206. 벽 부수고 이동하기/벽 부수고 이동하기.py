from collections import deque

def bfs():
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    q = deque()
    q.append([0, 0, 1])
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1
    
    while q:
        x, y, wall = q.popleft()
        
        if x == n-1 and y == m-1:
            return visited[x][y][wall]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                # If there is no wall
                if matrix[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    q.append([nx, ny, wall])
                
                # If there is a wall and you can break it
                elif matrix[nx][ny] == 1 and wall == 1:
                    visited[nx][ny][0] = visited[x][y][wall] + 1
                    q.append([nx, ny, 0])
    
    return -1

n, m = map(int, input().split())
matrix = [list(map(int, list(input().strip()))) for _ in range(n)]

print(bfs())