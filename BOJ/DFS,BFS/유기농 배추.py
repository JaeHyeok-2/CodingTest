import sys
from sys import stdin
from collections import deque

input = stdin.readline
sys.setrecursionlimit(10**4)

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def dfs(visited,board,r,c) :
    #if visited[r][c] :
     #   return
    visited[r][c] = True
    for i in range(4) :
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<row and 0<=nc < col :
            if not visited[nr][nc] and board[nr][nc] ==1 :
                visited[nr][nc] = True
                dfs(visited,board,nr,nc)

def bfs(visited,board,r,c) :
    q = deque([(r,c)])
    visited[r][c] = True
    while q:
        r,c = q.popleft()
        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr <row and 0<nc < col :
                if not visited[nr][nc] and board[nr][nc] == 1:
                    q.append([nr,nc])
                    visited[nr][nc] = True




for tc in range(int(input())) :
    col,row, k = map(int,input().split())
    visited = [[False] * col for _ in range(row)]
    #배추 1 땅 0
    board = [[0] * col for _ in range(row)]
    #배추 위치 심기
    for _ in range(k) :
        x,y = map(int,input().split()) # 가로,세로 로 입력을 받으므로
        board[y][x] =1
    #print(board)
    # 애벌레 수
    count = 0
    for i in range(row) :
        for j in range(col):
            if not visited[i][j] and board[i][j] == 1 :
                #dfs(visited,board,i,j)
                bfs(visited,board,i,j)
                count +=1
                #print((i,j))
    print(count)


