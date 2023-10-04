import sys
from collections import deque

input = sys.stdin.readline

N = int(input())  # 좌표 개수
x_cors = list(map(int, input().split()))  # x좌표 모음

def cor_sort(N, x_cors):
    sorted_unique_cors = sorted(set(x_cors))
    cor_to_idx = {cor: idx for idx, cor in enumerate(sorted_unique_cors)}
    return [cor_to_idx[cor] for cor in x_cors]

result = cor_sort(N, x_cors)
print(" ".join(map(str, result)))