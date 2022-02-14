# https://www.acmicpc.net/problem/11967
from collections import deque,defaultdict
from sys import stdin
input= stdin.readline

dr = [1,0,-1,0]
dc = [0,1,0,-1]

def bfs() :
    result = 1
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1
    lights = [[0] * n for _ in range(n)]
    lights[0][0] = 1
    q = deque([(0,0)])
    while q:
        r,c = q.popleft()
        for tr,tc in turnInfo[(r,c)] :
            if not lights[tr][tc] :
                lights[tr][tc] = 1
                result +=1

                for i in range(4) :
                    nr = tr + dr[i]
                    nc = tc + dc[i]
                    if 0<=nr<n and 0<=nc <n :
                        if visited[nr][nc] :
                            q.append((nr,nc))

        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr <n and 0<=nc <n :
                if not visited[nr][nc] and lights[nr][nc] :
                    q.append((nr,nc))
                    visited[nr][nc] = 1
    return result

n,m = map(int,input().split())
turnInfo =defaultdict(list)

for _ in range(m):
    sr, sc, tr, tc = map(int, input().split())
    turnInfo[(sr-1, sc-1)].append((tr-1, tc-1))

#print(turnInfo)
print(bfs())