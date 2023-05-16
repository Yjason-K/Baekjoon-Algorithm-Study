import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

# 부르트 포스, 전체 순열 구하기
permu = list(permutations(num, n))

# 문제에 주어진 수열 합 구하기 함수 구현
def calcul(arr, n):
    sum = 0
    for i in range(n-1):
        sum += abs(arr[i]-arr[i+1])
    return sum

max_sum = 0
# 전체 순열을 돌면서 최대값 찾기
for i in permu:
    max_sum = max(max_sum, calcul(i, n))

print(max_sum)