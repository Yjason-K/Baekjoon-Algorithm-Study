import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a = input().split()
    b = []
    for i in a:
        b.append(i[::-1])
    print(' '.join(b))