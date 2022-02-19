import sys
input = sys.stdin.readline
n = int(input())

dp = [[0] * n for _ in range(n)]
color = [list(map(int,input().split())) for _ in range(n)]

INF = int(1e9)

ans = INF
for start in range(3) :
    for i in range(3) :
        if i == start :
            dp[0][i] = color[0][i]
        else :
            dp[0][i] = INF

    for i in range(1,n) :
        dp[i][0] = color[i][0] + min(dp[i-1][1],dp[i-1][2])
        dp[i][1] = color[i][1] + min(dp[i-1][0],dp[i-1][2])
        dp[i][2] = color[i][2] + min(dp[i-1][0],dp[i-1][1])

    for i in range(3) :
        if start == i :
            continue
        ans = min(ans,dp[n-1][i])

print(ans)