import sys
from itertools import combinations as com
input = sys.stdin.readline

# 알파벳 갯수 L, 주어지는 알파벳 갯수 C
L, C = map(int, input().split())
words = list(map(str, input().split()))
words.sort() # 알파벳을 받아 오름차순 정렬 
vow = 'aeiou' # 모음 아에이오우

comb = com(words, L) # 모든 조합 찾기

for i in comb: 
    cnt = 0
    for j in i: # 모음이 있는경우 카운트
        if j in vow:
            cnt +=1
    
    # 최소 한 개의 모음 그리고 최소 두 개의 자음이 포함된 경우 확인
    if cnt >= 1 and cnt <= L-2:
        print(''.join(i))
