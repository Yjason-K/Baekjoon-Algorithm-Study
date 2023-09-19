def z(N, r, c):
    if N == 0:
        return 0
    
    half = 2 ** (N-1) # N을 2씩 나눠가며 좁혀나가기
    
    if r < half and c < half: # r,c 가 1사분면에 있을때
        return z(N-1, r, c)
    elif r < half and c >= half: # r,c 가 2사분면에 있을때
        return half**2 + z(N-1, r, c-half)
    elif r >= half and c < half: # r,c r가 3사분면에 있을때
        return 2 * (half**2) + z(N-1, r-half, c)
    else: # 4사분면 (r >= half and c >= half)
        return 3 * (half**2) + z(N-1, r-half, c-half)

N, r, c = map(int, input().split()) # 2^N, r행 c열
print(z(N, r, c))