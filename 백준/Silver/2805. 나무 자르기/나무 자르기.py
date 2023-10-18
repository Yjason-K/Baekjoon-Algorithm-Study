import sys
input = sys.stdin.readline

def cut():
    # 나무 길이 포인터
    start, end = 1, max(trees)
    
    while start <= end:
        mid = (start + end) // 2 # 나무자를 지점
        
        tree_length = 0
        
        for tree in trees:
            if tree > mid:
                tree_length += tree - mid
        
        if tree_length >= M:
            start = mid + 1
        else:
            end = mid -1
    
    return end


# 필요한 나무의 수 N, 팔요한 나무의 길이 M
N, M = map(int, input().split())
trees = list(map(int, input().split())) # 주어진 나무들

print(cut())