from sys import stdin

input = stdin.readline

n, m, x, y, l = map(int, input().split())
dice = [0] * 6
r,c = x,y
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
info = list(map(int,input().split()))
# (동,서,북,남 ) 순서로 1,2,3,4 로 입력이 주어진다.
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def rolling_dice(x, y, dir):
    global r, c
    if not (0 <= r + dx[dir - 1] < n and 0 <= c + dy[dir - 1] < m):
        return

    if dir == 1:
        dice[1],dice[3],dice[4],dice[5] = dice[4],dice[5],dice[3],dice[1]
    elif dir == 2:
        dice[1],dice[3],dice[4],dice[5] = dice[5],dice[4],dice[1],dice[3]
    elif dir == 3:
        dice[0],dice[1],dice[2],dice[3] = dice[1],dice[2],dice[3],dice[0]
    else:
        dice[0],dice[1],dice[2],dice[3] = dice[3],dice[0],dice[1],dice[2]

    nx = x + dx[dir - 1]
    ny = y + dy[dir - 1]
    r,c = nx, ny
    if board[nx][ny] != 0:
        dice[3] = board[nx][ny]
        board[nx][ny] = 0
    else:
        board[nx][ny] = dice[3]
    #print("현재 좌표 : {},{}".format(r,c))
    print(dice[1])


for i in info:
    rolling_dice(r, c, i)
    #print(dice)
