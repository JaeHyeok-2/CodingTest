# https://www.acmicpc.net/problem/11048
"""
문제 설명
    N x M 크기의 미로에 갇혀있을때, 미로는 1x1크기의 방으로 나누어져있고, 각방에는 사탕이 존재
    왼쪽상단은 (1,1), 맨아래는 (N,N)
    준규는 (1,1) ->(N,M)으로 이동하려고할때, 3,5,6시 방향으로 이동이가능하다.
    각 방을 방문할때 마다 방에 놓여져 잇는 사탕을 모두 가져갈 수 있을때, 준규가 N,M으로 이동할때 가져올 수 있는 사탕의 개수

"""

n,m = map(int,input().split())
board = []
for _ in range(n) :
    board.append(list(map(int,input().split())))

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1) :
    for j in range(1,m+1) :
        dp[i][j] = board[i-1][j-1] + max(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])

print(dp[n][m])