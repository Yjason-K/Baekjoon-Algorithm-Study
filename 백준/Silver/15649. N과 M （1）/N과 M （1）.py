import sys
input = sys.stdin.readline

def dfs(n, lst):
    # 종료조건 (n에 관련) + 정답 처리
    if n == M: # M개의 수열을 완성
        ans.append(lst)
        return
    
    # 하부 단계(함수) 호출
    for j in range(1, N+1):
        if v[j] == 0: # 선택되지 않은 숫자인 경우 추가 
            v[j] = 1
            dfs(n+1, lst+[j])
            v[j] = 0

N, M = map(int, input().split())
ans = [] # 정답 리스트
v = [0] * (N+1) # 중복을 확인할 visited 배열

dfs(0, [])
for lst in ans:
    print(*lst)