#   https://www.acmicpc.net/problem/3190 백준알고리즘 "뱀"
#   큐를 이용한 구현 문제
from collections import deque
n = int(input())    # 보드의 크기
k = int(input())    # 사과의 개수
board = [[0] *(n+1) for _ in range(n+1)] # 2차원 배열 생성

for _ in range(k) :
    r,c = map(int,input().split())
    board[r][c] = 1 # 사과가 있는 칸은 1로 배정

l = int(input())    #뱀의 방향 정보 개수
info = []    # 방향을 담을 배열
for _ in range(l) :
    x,c = input().split()
    info.append((int(x),c)) # x는 time, c 는 방향(direction)

# 동 남 서 북 4방향 : 초기뱀의 방향은 동쪽을 가르키므로 이순서로 지정
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction,c) :
    if c== "L" : # 반시계
        direction = (direction -1)%4
    else :
        direction = (direction +1)%4
    return direction


def simulation() :
    x,y =1,1 # 뱀의 시작지점 (1,1)
    time = 0
    direction = 0
    index = 0
    q = deque()
    q.append((x,y))
    board[x][y] =2 # 뱀의 위치를 2로 표현
    while True:
        nx = x + dx[direction] # 다음 움직일 칸의 x
        ny = y + dy[direction] # 다음 움직일 칸의 y
        if 1<=nx and 1<=ny and nx<=n and ny<=n and board[nx][ny] !=2 : # 보드 내에위치하고, 자신의 몸과 만나지않을경우
            if board[nx][ny] == 0 : # 사과가 아닌자리
                board[nx][ny] =2
                q.append((nx,ny))
                qx,qy = q.popleft()
                board[qx][qy] = 0 # 꼬리였던 위치는 다시 0 으로
            elif board[nx][ny] == 1:
                board[nx][ny] =2
                q.append((nx,ny)) # 사과를 먹으면 성장
        else :  #벽이거나, 자신의 몸을 마주쳤을경우
            time +=1
            break
        time +=1
        x,y = nx,ny # x,y 현재위치값 수정
        if( index < l and time == info[index][0]) : # 방향을 바꾸어야 할때,
            direction = turn(direction,info[index][1])
            index +=1

    return time

print(simulation())