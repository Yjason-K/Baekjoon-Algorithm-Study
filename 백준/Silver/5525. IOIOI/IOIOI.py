# 5525 IOIOI
import sys
input = sys.stdin.readline

N = int(input()) # Pn
M = int(input()) # S의 길이
S = input() # I와 O로만 이루어진 문자열
P = 'I' + "OI" * N

answer = 0
i = 0
while i < (M - 2*N):
    if S[i:i+2*N +1] == P:
      answer +=1
      i +=2
    else:
      i +=1

print(answer)