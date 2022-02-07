import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int,input().split())
board =  [list(input().strip()) for _ in range(n)]

rx,ry,bx,by = [0] *4

for i in range(n) :
    for j in range(m) :
        if board[i][j] == 'R' :
            rx,ry = i,j
        if board[i][j] == 'B' :
            bx,by = i,j

q = deque()
q.append((rx,ry,bx,by,0)) # 빨간구슬 rx,ry  파란구슬 bx,by 시간 0 초

visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
visited[rx][ry][bx][by] = True
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def move(x,y,_dx,_dy,count) :
    while board[x+_dx][y+_dy] !="#" and board[x][y] !='O' :
        x +=_dx
        y +=_dy
        count +=1
    return x,y,count

def bfs() :
    while q:
        _rx,_ry,_bx,_by,time = q.popleft()
        if time >=10 :
            break

        for i in range(4) :
            nrx,nry,rc = move(_rx,_ry,dx[i],dy[i],0)
            nbx,nby,bc = move(_bx,_by,dx[i],dy[i],0)

            if board[nbx][nby] == 'O':
                continue

            if board[nrx][nry] == 'O' :
                print(time+1)
                return


            if nrx ==nbx and nry == nby :
                if rc > bc :
                    nrx = nbx - dx[i]
                    nry = nby - dy[i]
                else :
                    nbx = nrx - dx[i]
                    nby = nby - dy[i]

            if not visited[nrx][nry][nbx][nby] :
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx,nry,nbx,nby,time+1))
    print(-1)

bfs()

