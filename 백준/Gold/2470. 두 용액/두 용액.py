def find_closest_pair(arr):
    left, right = 0, n - 1
    min_sum = float('inf')
    result_pair = []
    
    while left < right:
        # 현재 두 용액의 합 계산
        current_sum = arr[left] + arr[right]
        
        # 절댓값으로 가장 가까운 합을 갱신
        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            result_pair = [arr[left], arr[right]]
        
        # 합이 0보다 작다면 left를 증가시켜 더 큰 값으로 접근
        if current_sum < 0:
            left += 1
        # 합이 0보다 크다면 right를 감소시켜 더 작은 값으로 접근
        else:
            right -= 1
    
    return result_pair

n = int(input())
arr = list(map(int, input().split()))

# 입력 받은 용액들을 정렬
arr.sort()

closest_pair = find_closest_pair(arr)
print(closest_pair[0], closest_pair[1])

