import sys
from collections import deque
input =sys.stdin.readline

n,m = map(int,input().split())
board = []
for _ in range(n) :
    board.append(list(map(int,input().strip())))

dr = [1,0,-1,0]
dc = [0,1,0,-1]
def bfs() :
    q = deque()
    q.append([0,0,1])
    visit = [[[0,0] for _ in range(m)] for _ in range(n)] #  n ,m ,2 배열 생성
    visit[0][0][1] = 1

    while q :
        r,c,w = q.popleft()
        if r == n-1 and c == m-1 :
            return visit[r][c][w]

        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr<n and 0<=nc<m :
                #벽을 마주쳤을때, 부술수있다면
                if board[nr][nc] == 1 and w == 1 :
                    visit[nr][nc][0] = visit[r][c][w]+1
                    q.append([nr,nc,0])
                elif board[nr][nc] == 0 and visit[nr][nc][w] == 0 :
                    visit[nr][nc][w] = visit[r][c][w]+1
                    q.append([nr,nc,w])
    return -1
"""
if elif 문에서 몇가지를 생각해보았다.
만약 전의 칸에서 벽을 부수지않고 다음칸을 왔을때, w = 1인상태로 유지하며, q에 삽입
만약 전의 칸에서 벽을 부수고 다음칸에 왔다면 , 이후의 w값들은 계속 0 일것이다.

"""
print(bfs())

