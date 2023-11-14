import math 
def solution(r1, r2):
    points = 0
    for i in range(1, r2 + 1) :
        points += math.floor((r2**2 - i**2)**0.5) - math.ceil(max(0,r1**2 - i**2)**0.5) + 1
    return points*4