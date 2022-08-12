import sys
input= sys.stdin.readline
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

case = [
    # case 1
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    # case 2
    [[0, 0], [0, 1], [1, 0], [1, 1]],
    # case 3
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 0], [1, 0], [0, 1], [0, 2]],
    [[0, 0], [0, 1], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [0, 2], [-1, 2]],
    [[0, 0], [0, 1], [-1, 1], [-2, 1]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [1, 0], [2, 0]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    # case 4
    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [-1, 1], [-1, 2]],
    [[0, 0], [0, 1], [-1, 1], [1, 0]],
    [[0, 0], [0, 1], [1, 1], [1, 2]],
    # case 5
    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 0], [-1, 1], [0, 1], [1, 1]],
    [[0, 0], [0, 1], [0, 2], [-1, 1]],
    [[0, 0], [1, 0], [2, 0], [1, 1]]
]

max = 0

def check(sum) :
    global max
    if sum > max :
        max = sum

def tetromino(i,j):
    for x in range(19):
        sum = 0
        for y in range(4) :
            ni = i + case[x][y][0]
            nj = j + case[x][y][1]
            if 0<=ni<n and 0<=nj <m :
                sum +=board[ni][nj]
            else :
                break
        check(sum)


for i in range(n) :
    for j in range(m) :
        tetromino(i,j)
print(max)