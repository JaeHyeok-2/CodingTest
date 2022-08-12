# https://www.acmicpc.net/problem/14502
# DFS,완전탐색을 이용한 그래프문제
import copy
import sys
input= sys.stdin.readline
n,m = map(int,input().split())
board = []
temp = [[0]*m for _ in range(n)] # 벽을 세운후의 배열

for _ in range(m) :
    board.append(list(map(int,input().split()))) # 2차원 배열 입력

# 벽을 설치하고, 바이러스를 확산후의 0 의 개수 파악
def get_score() :
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score+=1
    return score
# 4방향 좌표
dr = [1,0,-1,0]
dc = [0,1,0,-1]
#바이러스 확산 dfs
def spread_virus(r,c):
    for i in range(4) :
        nr = r + dr[i]
        nc = c + dc[i]
        if nr>=0 and nc>=0 and nr<n and nc<m:
            if(temp[nr][nc] == 0) :
                temp[nr][nc] =2
                spread_virus(nr,nc)
#결과 변수
result = 0

def selectWall_and_DFS(count) :
    global result
    #count가 3이되면, dfs를 실행
    if count == 3:
        for i in range(n) :
            for j in range(m):
                temp[i][j] = board[i][j]
        for i in range(n) :
            for j in range(m):
                if temp[i][j] == 2:
                    spread_virus(i,j)
        result = max(result,get_score())
        return
    #벽이 3개 미만일 경우,
    else :
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:    #빈칸이라면
                    board[i][j] = 1     #벽을 세운후,
                    count +=1           #count 를 1증가
                    selectWall_and_DFS(count)   #재귀적으로 다시 호출
                    count-=1    #재귀가 끝나면 count를 다시 감소시킨후 원위치
                    board[i][j] = 0

selectWall_and_DFS(0)
print(result)