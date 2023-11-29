import sys
import heapq
input = sys.stdin.readline

def find_shortest_path(N, D, shortcuts):
    shortest_distances = [float('inf')] * (D + 1)
    shortest_distances[0] = 0  # 시작 지점의 거리는 0

    heap = []
    heapq.heappush(heap, (0, 0))  # (거리, 현재 위치)

    # 고속도로 진행 경로
    highway = [(i, i + 1, 1) for i in range(D)]

    while heap:
        current_distance, current_position = heapq.heappop(heap)

        # 현재 위치의 거리가 이미 처리된 경우 넘어감
        if shortest_distances[current_position] < current_distance:
            continue

        # 현재 위치에서 갈 수 있는 모든 경로 (지름길 + 고속도로 진행 경로) 탐색
        for start, end, distance in (shortcuts + highway):
            if start == current_position and end <= D:
                new_distance = current_distance + distance
                if new_distance < shortest_distances[end]:
                    shortest_distances[end] = new_distance
                    heapq.heappush(heap, (new_distance, end))

    return shortest_distances[D]

N, D = map(int, input().split())
shortcuts = [ list(map(int, input().split(' '))) for _ in range(N) ]
print(find_shortest_path(N, D, shortcuts))