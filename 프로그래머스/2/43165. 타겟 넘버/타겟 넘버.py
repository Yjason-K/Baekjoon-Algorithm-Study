from collections import deque

def solution(numbers, target):
    answer = 0
    
    # bfs를 돌리기 위한 que
    que = deque()
    len_numbers = len(numbers)
    # 처음 값도 음수 양수 지정 필요하기 때문에 
    que.append([numbers[0],0])
    que.append([-1*numbers[0],0])
    
    while que:
        # idx를 1씩 늘려가며 cur을 업데이트 해서 cur이 target이 되는 경우
        cur, idx = que.popleft()
        idx += 1
        # idx가 아직 배열 길이보다 짧으면 이어서 진행
        if idx < len_numbers:
            que.append([cur+numbers[idx], idx])
            que.append([cur-numbers[idx], idx])
        else:
            if cur == target and idx == len_numbers:
                answer += 1
    return answer