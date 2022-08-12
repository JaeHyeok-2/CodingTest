import heapq
import sys
input = sys.stdin.readline
w,h = map(int,input().split())

board = [list(input().strip()) for _ in range(h)]
visited= [[int(1e9)] * w for _ in range(h)]

laser = []
for i in range(h) :
    for j in range(w) :
        if board[i][j] == 'C' :
            laser.append((i,j))

sx,sy = laser[0]
ex,ey = laser[1]
heap = []
visited[sx][sy] = 0

dx = (1,0,-1,0)
dy = (0,1,0,-1)
def dfs() :
    heapq.heappush(heap,(0,sx,sy))

    while heap:
        d,x,y = heapq.heappop(heap)
        visited[x][y] = d
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            while True :
                if not(0<=nx<h and 0<=ny<w) :
                    break
                if board[nx][ny] == '*' :
                    break
                if visited[nx][ny] < visited[x][y] +1 :
                    break

                visited[nx][ny] = visited[x][y] +1
                heapq.heappush(heap,(visited[x][y]+1,nx,ny))
                nx += dx[i]
                ny += dy[i]
                if visited[ex][ey] != int(1e9) :
                    return
dfs()
print(visited[ex][ey]-1)
