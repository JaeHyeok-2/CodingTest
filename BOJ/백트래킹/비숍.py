"""
1. 흑백을 나눌줄 알아야함
2. 체스판을 따로만들자
"""
import sys
input= sys.stdin.readline
n = int(input())
color = [[0] * n for _ in range(n)]
chess_map = []
black,white = [],[]

for i in range(n) :
    for j in range(n) :
        color[i][j] = (i%2 == 0 and j%2== 0) or (i%2 != 0 and j%2 !=0)

#print(color)

for i in range(n) :
    chess_map.append(list(map(int,input().split())))
    for j in range(n) :
        # 1일경우는 Black Board
        if chess_map[i][j] == 1 and color[i][j] ==1 :
            black.append([i,j])
        elif chess_map[i][j] == 1 and color[i][j] ==0  :
            white.append([i,j])

black_cnt,white_cnt = [0] *2

isUsed1 = [0] *(2 *n -1)
isUsed2 = [0] *(2 *n -1)


def fun(bishop,index,count) :
    global black_cnt,white_cnt
    if index == len(bishop) :
        rx,ry = bishop[index-1]
        # black 칸일경우
        if color[rx][ry]  :
            black_cnt = max(black_cnt,count)
        else :
            white_cnt = max(white_cnt,count)
        return
    x,y =bishop[index]

    # x,y는 현재 비숍의 좌표
    if isUsed1[x+y] or isUsed2[x-y+n-1] : # 현재 놓으려고하는 좌표에 놓을 수 없을 경우,
        fun(bishop,index+1,count)
    else :
        isUsed1[x+y] = 1
        isUsed2[x-y+n-1] = 1
        fun(bishop,index+1,count+1)
        isUsed1[x+y] = 0
        isUsed2[x-y+n-1] = 0
        # 현재좌표에 그냥 안놓을수도 있으므로 아닐경우도
        fun(bishop,index+1,count)

if len(black) > 0 :
    fun(black,0,0)
if len(white) > 0 :
    fun(white,0,0)
print(black_cnt + white_cnt)


