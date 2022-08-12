import copy
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
cctv = []
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]
# 북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]



for i in range(n) :
    for j in range(m) :
        if board[i][j] in [1,2,3,4,5] :
            cctv.append((board[i][j],i,j))


def search(dir_mode,x,y,arr):
    for i in dir_mode :
        nx = x
        ny = y
        while True :
            nx += dx[i]
            ny += dy[i]
            if not(0<=nx<n and 0<=ny<m) :
                break
            if arr[nx][ny] == 6 :
                break
            elif arr[nx][ny] == 0 :
                arr[nx][ny] =7


def dfs(depth,arr) :
    global min_value
    if depth == len(cctv) :
        count = 0
        for i in range(n) :
            count +=arr[i].count(0)
        min_value = min(min_value,count)

        return

    temp = copy.deepcopy(arr)
    cctv_num,x,y = cctv[depth]
    for i in mode[cctv_num] :
        search(i,x,y,temp)
        dfs(depth+1,temp)
        temp = copy.deepcopy(arr)




min_value = int(1e9)

dfs(0,board)
print(min_value)