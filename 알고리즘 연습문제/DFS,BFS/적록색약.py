from sys import stdin
from collections import deque
input= stdin.readline

n = int(input())
board = [list(input().strip()) for _ in range(n)]
#적록색약 = 빨강 초록이 같은색으로 보임

visited = [[False]*n for _ in range(n)]

red = 0
green = 0
blue = 0

dr = (1,0,-1,0)
dc = (0,1,0,-1)

def bfs(i,j,color) :
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    while q:
        r,c = q.popleft()
        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr <n and 0 <=nc < n :
                if not visited[nr][nc] and board[nr][nc] == color :
                    q.append((nr,nc))
                    visited[nr][nc] = True


for i in range(n) :
    for j in range(n) :
        if not visited[i][j] :
            if board[i][j] == 'R' :
                bfs(i,j,'R')
                red+=1
            elif board[i][j] == 'B' :
                bfs(i,j,'B')
                blue +=1
            else :
                bfs(i,j,'G')
                green +=1

normal = red + blue + green


visited = [[False]*n for _ in range(n)]

for i in range(n) :
    for j in range(n) :
        if board[i][j] == 'R':
            board[i][j] = 'G'


#print(board)

blue,green = 0,0
for i in range(n) :
    for j in range(n) :
        if not visited[i][j] :
            if board[i][j] == 'B' :
                bfs(i,j,'B')
                blue +=1
            elif board[i][j] == 'G':
                bfs(i,j,'G')
                green +=1

print(normal,green+blue)