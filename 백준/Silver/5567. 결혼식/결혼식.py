import sys
from collections import deque
input= sys.stdin.readline

def wedding():
    visited = [0] * (n+1)
    q = deque()
    q.append(1)
    visited[1] = 1
    
    while q:
        cur = q.popleft()
        for friend in realtionship[cur]:
            if visited[friend] == 0:
                q.append(friend)
                visited[friend] = visited[cur] + 1
   
    invite = 0
    # 상근이 친구 또는 상근이 친구의 친구 / 본인 제외
    for i in range(2, n+1):
        if visited[i] != 0 and visited[i] < 4:
            invite +=1
            
    return invite

n = int(input()) # 동기 수
m = int(input()) # 관계 수
realtionship = [ [] for _ in range(n+1) ] # 친구관계
# 친구관계 추가하기
for _ in range(m):
    a, b = map(int, input().split())
    realtionship[a].append(b)
    realtionship[b].append(a)

print(wedding())
        
        
    