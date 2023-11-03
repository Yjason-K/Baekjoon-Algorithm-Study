import sys
input = sys.stdin.readline

def ill_knight():
    if N == 1:
        return 1
    elif N == 2:
        return min(4, (M-1)//2 + 1)
    elif M <= 6:
        return min(4, M)
    else:
        return (2 + (M-5)) + 1

N, M = map(int, input().split())
print(ill_knight())