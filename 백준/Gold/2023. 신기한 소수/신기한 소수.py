# 파이썬 재귀제한 변경
import sys
sys.setrecursionlimit(1000000)

# 자리 수 입력받기
n = int(input())


# 소수 판별함수 구현
def is_Prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False


    return True


# dfs 함수 재귀함수로 구현
def DFS(num):
    if len(str(num)) == n:
        print(num)


    for i in [1, 3, 5, 7, 9]:
        if is_Prime(num * 10 + i):
            DFS(num * 10 + i)

# 처음 자리수로 들어올수 있는 수들을 DFS에 입력해주기
DFS(2)
DFS(3)
DFS(5)
DFS(7)