import sys
from collections import deque
input = sys.stdin.readline

# bfs 탐색을 통한 동생의 위치 찾기


def short_time():
    que = deque()
    # 순간이동의 경우 2배가 되기때문에 방문배열을 200000까지
    visited = [0] * 100001

    que.append(N)  # 수빈이 위치로 시작
    visited[N] = 1  # 시작위치, 1초부터 시작

    # bfs
    while que:
        cur_position = que.popleft()

        # 현재 위치가 동생위치라면 그때의 방문초 return하기
        if cur_position == K:
            return visited[K] - 1  # 1초부터 시작 했기 때문에 - 1

        for next_position in (cur_position-1, cur_position+1, cur_position*2):
            if 0 <= next_position <= 100000 and visited[next_position] == 0:
                que.append(next_position)
                visited[next_position] = visited[cur_position] + 1

    return -1  # 동생 위치에 도달하지 못하는 경우


# 수빈이 위치, 동생 위치
N, K = map(int, input().split())

print(short_time())

