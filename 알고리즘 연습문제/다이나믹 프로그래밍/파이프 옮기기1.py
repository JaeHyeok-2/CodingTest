from sys import stdin
input = stdin.readline

n = int(input())
board = []
for _ in range(n) :
    board.append(list(map(int,input().split())))

# 0 : 가로 , 1 : 세로 , 2 : 대각선
dp = [[[0] * n for _ in range(n)] for _ in range(3)]

dp[0][0][1] = 1

for i in range(2,n):
    dp[0][0][i] = dp[0][0][i-1]

# col = 0인 세로줄은 사용 불가
for i in range(1,n) : # 두번째 행 부터
    for j in range(2,n): # 첫번째 파이프 때문에, 3행부터 시작할 수 밖에 없음
        if board[i][j] == 0 and board[i-1][j] == 0 and board[i][j-1] == 0 :
            dp[2][i][j] = dp[2][i-1][j-1] + dp[1][i-1][j-1] + dp[0][i-1][j-1]

        if board[i][j] == 0 :
            #가로 일경우 ㅡ ㅡ
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            # 세로 일경우 : 가로에서는 올수 없음,  대각선, 세로 에서만
            dp[1][i][j] = dp[2][i-1][j] + dp[1][i-1][j]

print(sum(dp[i][n-1][n-1] for i in range(3)))