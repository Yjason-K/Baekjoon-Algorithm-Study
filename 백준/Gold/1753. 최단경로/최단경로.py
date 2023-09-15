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
    # 방문배열 초기화
    visited = [False] * (V+1)
    
    # 정답배열 10e9 초기화 및 시작지점 0 설정
    answer = [10e9] * (V+1)
    answer[start] = 0
    
    # 우선순위 큐 초기화: 시작 노드의 거리 정보 추가 (거리, 노드 번호)
    pq = [(0, start)]
    
    # 우선순위 큐가 비어있지 않다면 계속 진행
    while pq:
        # 현재 노드의 거리와 현재 노드
        curr_dist, curr_node = heapq.heappop(pq)
        
        # 이미 방문한 곳이면 넘어가기
        if visited[curr_node]:
            continue
        
        # 현재 노드를 방문 처리
        visited[curr_node] = True
        
        # 현재 노드에 연결된 모든 인접 노드를 순회
        for adj_node, weight in graph[curr_node]:
            # 시작 노드부터 인접 노드까지의 총 거리 계산
            distance = curr_dist + weight
            
            # 계산된 거리가 기존에 저장된 거리보다 짧은 경우
            if answer[adj_node] > distance:
                # 최단 거리를 업데이트
                answer[adj_node] = distance
                # 인접 노드의 거리 정보를 우선순위 큐에 추가
                heapq.heappush(pq, (distance, adj_node))
                
    return answer


result = dijkstra(V, E, start, graph)
            
#최단거리 구한 경로 출력하기
for j in range(1, V+1):
    if result[j] == 10e9:
        print("INF")
    else:
        print(result[j])