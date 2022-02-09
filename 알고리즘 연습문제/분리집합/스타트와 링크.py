import sys
from itertools import combinations
input =sys.stdin.readline


n = int(input())
number = [i for i in range(n)]
players = []
for _ in range(n) :
    players.append(list(map(int,input().split())))

result = 1e9
for r1 in combinations(number,n//2) :
    start,link =0,0
    r2 = list(set(number) - set(r1))
    for r in combinations(r1,2) :
        start +=players[r[0]][r[1]]
        start +=players[r[1]][r[0]]

    for r in combinations(r2,2):
        link +=players[r[0]][r[1]]
        link +=players[r[1]][r[0]]
    result = min(result,abs(start-link))

print(result)

