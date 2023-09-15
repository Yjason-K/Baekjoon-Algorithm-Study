import sys
import heapq
input = sys.stdin.readline

# 정점과 간선의 갯수
V, E = map(int, input().split())
start = int(input()) # 최소 경로를 위한 시작지점
# 간선 그래프
graph = [ [] for _ in range(V+1) ]
for _ in range(E):
    # a에서 b로 가는 가중치 c인 간선
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(V, E, start, graph):
    # 방문한곳은 다시 안가도록
    visited = [False] * (V+1)
    # 최단거리 정답 배열
    answer = [10e9] * (V+1)
    answer[start] = 0
    
    # 우선순위 큐를 사용하여 시작 노드 정보 추가 (거리, 노드 번호)
    pq = [(0, start)]
    
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        
        if visited[curr_node]:
            continue
        
        visited[curr_node] = True
        
        for adj_node, weight in graph[curr_node]:
            distance = curr_dist + weight
            
            if answer[adj_node] > distance:
                answer[adj_node] = distance
                heapq.heappush(pq, (distance, adj_node))
                
    return answer


result = dijkstra(V, E, start, graph)
            
#최단거리 구한 경로 출력하기
for j in range(1, V+1):
    if result[j] == 10e9:
        print("INF")
    else:
        print(result[j])