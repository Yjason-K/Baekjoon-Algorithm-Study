import sys
input = sys.stdin.readline

def solution():
    start = min(moneys)
    end = sum(moneys)

    while start <= end:
        mid = (start + end) // 2
        money = mid
        cnt = 1
        
        for i in moneys:
            if money - i < 0:
                money = mid
                cnt += 1
            money -= i
            
        if cnt > M or mid < max(moneys):
            start = mid + 1
        else:
          end = mid - 1
          ans = mid

    return ans

N, M = map(int, input().split())
moneys = [ int(input()) for _ in range(N) ]

print(solution())