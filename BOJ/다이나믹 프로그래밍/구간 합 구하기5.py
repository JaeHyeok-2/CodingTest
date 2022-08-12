# https://www.acmicpc.net/problem/11660
from sys import stdin
input = stdin.readline
n,m = map(int,input().split())

board = [[0]*(n+1)]
for _ in range(n) :
    nums= [0] + list(map(int,input().split()))
    board.append(nums)

#사각형 구간합 만들기 1) 열 누적합
for i in range(1,n+1):
    for j in range(n):
        board[i][j+1] +=board[i][j]

# 2) 행 누적합
for j in range(1,n+1):
    for i in range(n):
        board[i+1][j] +=board[i][j]

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    print(board[x2][y2] - board[x1-1][y2] - board[x2][y-1] +board[x1-1][y1-1])
