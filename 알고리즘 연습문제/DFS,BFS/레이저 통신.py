import sys
from collections import deque
input= sys.stdin.readline
INF = int(1e4)

w,h = map(int,input().split())
board = [input().rstrip() for _ in range(h)]
visited = [[INF]*w for _ in range(h)]
start = []

for i in range(h) :
    for j in range(w) :
        if board[i][j] == 'C' :
            start.append((i,j))

(sr,sc),(er,ec) = start

dx = [1,0,-1,0]
dy = [0,1,0,-1]
def bfs(x,y) :
    visited[x][y] = 0
    q = deque([(x,y)])
    while q :
        r,c = q.popleft()
        for i in range(4) :
            nr = r + dx[i]
            nc = c + dy[i]
            while True :
                if not ( 0<=nr < h and 0<= nc < w) :
                    break
                if board[nr][nc] == '*' :
                    break
                if visited[nr][nc] < visited[r][c]+ 1:
                    break
                visited[nr][nc] = visited[r][c] +1
                q.append((nr,nc))
                nr += dx[i] # 한칸전진
                nc += dy[i]

bfs(sr,sc)
print(visited[er][ec]-1)

