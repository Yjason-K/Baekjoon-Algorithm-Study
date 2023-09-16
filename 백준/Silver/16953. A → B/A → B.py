import sys
input = sys.stdin.readline

def min_cnt(A, B):
    cnt = 0  # 계산횟수
    
    # B를 A값에 가깝게 줄여나가면서 B > A때 까지 갱신
    while B > A:
        cnt += 1
        # 마지막 자리가 1인 경우는 10나눠버리기 (몫만 얻기)
        if str(B)[-1] == '1':
            B //= 10
        elif B % 2 == 0:  # 아니면 2 나누기
            B //= 2
        else: # 홀수이면서 마지막 자리가 1이 아닌 경우
            return -1
        
        if B == A:
            return cnt + 1  # 홀수이면서 마지막 자리가 1이 아닌 경우
    
    # B로 A를 못만드는 경우
    return -1

A, B = map(int, input().split())
print(min_cnt(A, B))
