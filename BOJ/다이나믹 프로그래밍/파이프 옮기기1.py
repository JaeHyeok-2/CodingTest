n = int(input())
board = [[] for _ in range(n)]

for i in range(n) :
    board[i] = list(map(int,input().split()))

dp = [[[0]*n for _ in range(n)] for _ in range(3)]
dp[0][0][1] =1

# 0 : 가로, 1 : 세로, 2 : 대각선
for i in range(2,n) :
    if board[0][i] == 0 :
        dp[0][0][i] = dp[0][0][i-1]

for i in range(1,n) :
    for j in range(2,n) :
        if board[i][j] == 0 and board[i-1][j] == 0 and board[i][j-1] == 0 :
            dp[2][i][j] = dp[2][i-1][j-1] + dp[1][i-1][j-1] + dp[0][i-1][j-1]
        # 가로일경우
        if board[i][j] == 0 :
            dp[0][i][j] = dp[2][i][j-1] + dp[0][i][j-1]
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]

print(sum(dp[i][n-1][n-1] for i in range(3)))
