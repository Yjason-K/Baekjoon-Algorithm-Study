# 조합을 이용한 문제풀이
import sys
from itertools import combinations as comb
input = sys.stdin.readline

n = int(input())  # 인원
graph = [list(map(int, input().split())) for _ in range(n)]  # 능력치 그래프
members = [i for i in range(n)]
answer = 10e9

for t1 in comb(members, n//2):  # 멤버애서 n/2명인 조합을 만들어 team1을 만들기
    start, link = 0, 0
    t2 = list(set(members) - set(t1))  # team1을 제외한 멤버를 team2
    for r in comb(t1, 2):  # 팀에서 2명씩 뽑아 능력치 추가
        start += graph[r[0]][r[1]]
        start += graph[r[1]][r[0]]
    for r in comb(t2, 2):
        link += graph[r[0]][r[1]]
        link += graph[r[1]][r[0]]

    answer = min(answer, abs(start-link))  # 최솟값을 찾아가기

print(answer)
