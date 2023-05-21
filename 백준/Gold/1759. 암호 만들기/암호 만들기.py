import sys
from itertools import combinations as com
input = sys.stdin.readline

L, C = map(int, input().split())
words = list(map(str, input().split()))
words.sort()
vow = 'aeiou'

comb = com(words, L)

for i in comb:
    cnt = 0
    for j in i:
        if j in vow:
            cnt +=1
            
    if cnt >= 1 and cnt <= L-2:
        print(''.join(i))
