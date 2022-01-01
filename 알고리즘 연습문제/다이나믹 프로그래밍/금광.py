import sys
input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())  # n x m  행렬
    data = list(map(int, input().split()))
    dp = []
    index = 0
    for i in range(n):
        dp.append(data[index: index + m])
        index += m

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0 # 첫번째 행에서는 위에서 내려오는것이 없음
            else:
                left_up = dp[i - 1][j - 1]

            if i == n - 1:  #마지막 행에서는 더이상 밑의 행이 없으므로 밑에서 올라오는 것이 없음
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]

            left = dp[i][j - 1]

            dp[i][j] = dp[i][j] + max(left_up, left, left_down)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)
