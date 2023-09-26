import sys
from heapq import heappush, heappop
INF = sys.maxsize
input = sys.stdin.readline


def dijkstra():

    # 2차원 다익스트라 배열. 현재 i에서 포장을 j개 했을 때 드는 최소거리
    distance = [[INF] * (K+1) for _ in range(N+1)]
    heap = []
    for i in range(K+1):
        distance[1][i] = 0
    heappush(heap, (0, 1, 0))

    # 다익스트라
    while heap:
        now_dist, now, v = heappop(heap)
        if distance[now][v] < now_dist:
            continue

        # 현재 정점에서 포장이 가능한 경우
        if v + 1 <= K:  # 조건 수정
            for (next, next_dist) in nodes[now]:
                if distance[next][v+1] > now_dist:
                    distance[next][v+1] = now_dist
                    heappush(heap, (now_dist, next, v+1))

        # 기본적으로 포장을 하지 않는경우
        for (next, next_dist) in nodes[now]:
            if distance[next][v] > now_dist + next_dist:
                distance[next][v] = now_dist + next_dist
                heappush(heap, (now_dist + next_dist, next, v))

    ans = INF
    for i in range(K+1):
        ans = min(ans, distance[N][i])
    return ans


# 도시의수 N, 도로의 수 M, 포장할 도로수 K
N, M, K = map(int, input().split())

# 도로 정보
nodes = [[] for _ in range(N+1)]
for _ in range(M):
    # 출발도시, 도착 도시, 걸리는 시간
    start, end, t = map(int, input().split())
    nodes[start].append((end, t))
    nodes[end].append((start, t))

print(dijkstra())