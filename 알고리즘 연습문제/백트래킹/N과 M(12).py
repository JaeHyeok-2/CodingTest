from sys import stdin
input = stdin.readline

n = int(input())
board = []
for _ in range(n) :
    board.append(list(map(int,input().split())))

result = [[[0]*n for _ in range(n)] for _ in range(3)]
result[0][0][1] = 1
for i in range(2,n) :
    if board[0][i] == 0 :
        result[0][0][i] = result[0][0][i-1]

for i in range(1,n) :
    for j in range(2,n) :
        if board[i][j] == 0 and board[i][j-1] == 0 and board[i-1][j] == 0 :
            result[2][i][j] = result[0][i-1][j-1] + result[1][i-1][j-1] + result[2][i-1][j-1]

        if board[i][j] == 0 :
            result[0][i][j] = result[0][i][j-1] + result[2][i][j-1]

            result[1][i][j] = result[0][i-1][j] + result[2][i-1][j]

print(sum(result[i][n-1][n-1] for i in range(3)))