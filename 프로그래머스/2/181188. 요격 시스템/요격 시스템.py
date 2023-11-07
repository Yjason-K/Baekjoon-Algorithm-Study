def solution(targets):
    # 미사일 끝나는 지점에 대한 오름차순 정렬
    targets.sort(key=lambda x: x[1])
    
    # 현재 미사일의 시작점이 이전에 요격한 폭격 미사일의 끝점보다 크거나 같으면 요격 미사일을 발사
    cnt, end = 0, 0
    for s, e in targets:
        if s >= end:
            cnt += 1
            end = e
    return cnt
