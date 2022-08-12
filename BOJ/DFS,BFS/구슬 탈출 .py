from sys import stdin
from collections import deque
input = stdin.readline

n,m = map(int,input().split())
board = [list(input().strip()) for _ in range(n)]

dx ,dy = (1,0,-1,0),(0,1,0,-1)
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
_rx,_ry,_bx,_by = [0] * 4
q = deque()


def init() :
    for i in range(n) :
        for j in range(m) :
            if board[i][j] == 'R' :
                _rx,_ry = i,j
            if board[i][j] == 'B' :
                _bx,_by = i,j

    q.append((_rx,_ry,_bx,_by,0)) # red,blue 구슬, time 정보
    visited[_rx][_ry][_bx][_by] = True


def move(_x,_y,_dx,_dy,c) :
    while board[_x][_y] != 'O' and  board[_x+_dx][_y+_dy] != '#':
        c+=1
        _x +=_dx
        _y +=_dy
    return _x,_y,c

def bfs() :

    while q:
        rx, ry, bx, by, time = q.popleft()
        if time >=10 :
            break
        for i in range(4) :
            nrx,nry,rc = move(rx,ry,dx[i],dy[i],0)
            nbx,nby,bc = move(bx,by,dx[i],dy[i],0)

            if board[nbx][nby] == 'O' :
                continue
            if board[nrx][nry] == 'O' :
                print(1)
                return

            if nrx == nbx and nry == nby :
                if rc > bc :
                    nrx = nbx - dx[i]
                    nry = nby - dy[i]
                else :
                    nbx = nrx - dx[i]
                    nby = nry - dy[i]

            if not visited[nrx][nry][nbx][nby] :
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx,nry,nbx,nby,time+1))
    print(0)

init()
bfs()


