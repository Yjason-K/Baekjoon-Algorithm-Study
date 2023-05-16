import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

# 뒤에서 부터 값을 조회하며 i이 i-1보다 작은 경우 찾기(target)
for i in range(n-1, 0, -1):
    if num[i-1] > num[i]:
        target = i-1
        for j in range(n-1, 0, -1):
            # 다시 뒤부터 순회하며 i-1일 때 보다 작은 값 위치 바꾸어 주기
            if num[target] > num[j]:
                num[target], num[j] = num[j], num[target]
                # target을 기준으로 배열을 나누고 뒤 부분은 새로 정렬하기, 내림차순
                answer = num[:target+1] + sorted(num[target+1:], reverse=True)
                print(*answer)
                exit() # 정답을 찾았기 때문에 코드 종료

# 그외의 경우 -1 출력
print('-1')