import sys
input = sys.stdin.readline


def count_steps():
    plus = []  # 양수 위치
    minus = []  # 음수 위치
    steps = 0  # 걸음수

    # 양수와 음수 위치 분리
    for i in books:
        if i < 0:
            minus.append(i)
        else:
            plus.append(i)

    # 양수와 음수를 절대값 기준 내림차순 정렬
    plus.sort(reverse=True)
    minus.sort()

    # 양수 그룹 처리
    for i in range(0, len(plus), M):
        # M개씩 묶어서 이동 거리 계산 (왕복 거리로 2를 곱함)
        steps += plus[i] * 2

    # 음수 그룹 처리
    for i in range(0, len(minus), M):
        # M개씩 묶어서 이동 거리 계산 (왕복 거리로 2를 곱함)
        steps += abs(minus[i]) * 2

    # 가장 멀리 있는 책은 마지막으로 이동시키므로, 돌아오는 거리는 빼줌
    steps -= max(max(plus, default=0), abs(min(minus, default=0)))

    return steps




# 옮겨 하는 책 N개, 한번에 들 수 있는 책 M개
N, M = map(int, input().split())
books = list(map(int, input().split()))  # 책의 위치

print(count_steps())