# bfs로 돌리기
# 전체 그래프를 bfs 돌려서 방문배열을 가지고 문제 풀기

from collections import deque, Counter


def bfs(visited, land, i, j, count):
    que = deque([(i, j)])
    visited[i][j] = count

    while que:
        cur_i, cur_j = que.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = cur_i + di, cur_j + dj
            if 0 <= ni < len(land) and 0 <= nj < len(land[0]) and land[ni][nj] == 1 and visited[ni][nj] == 0:
                que.append((ni, nj))
                visited[ni][nj] = count

    return visited


def solution(land):
    m, n = len(land[0]), len(land)
    count = 1
    visited = [[0] * m for _ in range(n)]

    # bfs를 통한 방문한 섬 만들기
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                visited = bfs(visited, land, i, j, count)
                count += 1

    # 방문배열 펼쳐서 섬의 갯수들 확인
    flat_visited = [num for row in visited for num in row if num > 0]
    count_of_numbers = Counter(flat_visited)

    # 행과 열을 바꿔 돌리기
    answer = []
    for i in range(m):
        check_num = []
        for j in range(n):
            if visited[j][i] > 0 and visited[j][i] not in check_num:
                check_num.append(visited[j][i])

        oil = 0
        for k in check_num:
            oil += count_of_numbers[k]

        answer.append(oil)

    return max(answer)