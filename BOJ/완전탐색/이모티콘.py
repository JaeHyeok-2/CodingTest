import sys
from collections import deque
input = sys.stdin.readline


dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y,num) :
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    island[x][y] = num
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx < n  and 0<=ny <n :
                if not visited[nx][ny] and board[nx][ny] == 1  :
                    island[nx][ny] = num
                    visited[nx][ny] = True
                    q.append([nx,ny])

def bfs2(num,q,distArr) :
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<ny<n :
                if board[nx][ny] == 0 and distArr[nx][ny] == 0 :
                    q.append([nx,ny])
                    distArr[nx][ny] = distArr[x][y] +1
                if board[nx][ny] == 1 and island[nx][ny] != num :
                    return distArr[x][y] -1


cnt = 1
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] *n for _ in range(n)]
island = [[0] * n for _ in range(n)]

for i in range(n) :
    for j in range(n) :
        if not visited[i][j] and board[i][j] != 0 :
            bfs(i,j,cnt)
            cnt+=1

# for i in range(n) :
#     print(island[i])

res = sys.maxsize
for k in range(1,cnt) :
    queue = deque()
    dist =[[0] * n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            if island[i][j] == k and board[i][j] == 1:
                queue.append([i,j])
                dist[i][j] = 1
    temp = bfs2(k,queue,dist)
    res = min(res,temp)

print(res)


