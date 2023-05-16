from itertools import permutations
n = int(input())

a = [i for i in range(1, n+1)]

for i in permutations(a, n):
    print(*list(i))