#   https://www.acmicpc.net/problem/1007
import sys
from itertools import combinations
input = sys.stdin.readline

for _ in range(int(input())) :
    n = int(input())
    p = []
    x_total,y_total = 0,0
    for _ in range(n) :
        x,y = map(int,input().split())
        x_total +=x
        y_total +=y
        p.append((x,y))

    v_lists = combinations(p,n//2) # Vector list combinations

    res = sys.maxsize
    for v_list in v_lists :
        x1_total,y1_total = 0,0
        for vx,vy in v_list :
            x1_total +=vx
            y1_total +=vy

        x2_total = x_total - x1_total
        y2_total = y_total - y1_total
        res = min(res, ((x2_total - x1_total)**2 + (y2_total-y1_total)**2) **0.5)

    print('{0:.12f}'.format(res))
