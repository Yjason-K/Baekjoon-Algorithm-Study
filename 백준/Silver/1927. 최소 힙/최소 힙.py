import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# 파이썬에서 힙은 최소힙!!
# 연산갯수 N
N = int(input())
heap = [] # 힙 배열 만들기

for _ in range(N):
    x = int(input()) # 정수 X입력
    if x == 0: # x가 0이라면 배열에서 가장 작은 값을 출력
        if heap != []:
            print(heappop(heap))
        else: # heap이 비어있는경우
            print(0)
    else: # 자연수를 입력 받은 경우 힙에 추가하기
        heappush(heap, x)