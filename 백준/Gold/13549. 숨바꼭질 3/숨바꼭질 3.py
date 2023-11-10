from collections import deque
import sys
input = sys.stdin.readline

# bfs를 통한 동생을 찾는 빠른 시간 찾기
def bfs(N, K):
    visited = [0] * 100001  # 방문을 기록할 리스트를 생성, 위치 X는 0 ≤ X ≤ 100,000 범위를 가짐
    que = deque([N])  # BFS를 위한 큐를 생성하고 시작 위치인 N을 넣어줌

    while que:
        cur = que.popleft()  # 현재 위치
        if cur == K:  # 동생의 위치에 도달했다면 함수를 종료하고 걸린 시간을 반환
            return visited[cur]

        # 가능한 모든 이동을 시도
        for next in (cur - 1, cur + 1, cur * 2):
            # 다음 위치가 유효한 범위 내에 있고 아직 방문하지 않았다면
            if 0 <= next < 100001 and not visited[next]:
                if next == cur * 2 and cur != 0:
                    visited[next] = visited[cur]  # 순간이동은 0초 후에 이동하므로 시간을 더하지 않음
                    que.appendleft(next)  # 순간이동한 위치를 큐의 앞부분에 추가
                else:
                    visited[next] = visited[cur] + 1  # 걸어서 이동하는 경우 시간을 1초 더함
                    que.append(next)  # 걸어서 이동한 위치를 큐의 뒷부분에 추가



# N 수빈이 위치, M 동생 위치
N, K = map(int, input().split())
print(bfs(N, K))