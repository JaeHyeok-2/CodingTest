import sys
from collections import deque

input = sys.stdin.readline
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)


def bfs(check):
    q = deque()
    count = 0
    for i in range(n):
        for j in range(n):
            if check[i][j]:
                count += 1
                q.append((i, j))
                while q:
                    x,y = q.popleft()
                    check[x][y] = False
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n:
                            if check[nx][ny]:
                                q.append((nx, ny))
                                check[nx][ny] = False
    return count


n = int(input())
board = []
rain = []
for i in range(n):
    data = list(map(int, input().split()))
    board.append(data)
    for j in range(n):
        if data[j] not in rain:
            rain.append(data[j])

rain.sort()
rain.append(rain[0]-1)
rain.sort()
result = 0

for height in rain:
    check = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 안전한 지역들은 True / 물에 잠긴지역은 False
            if board[i][j] > height:
                check[i][j] = True

    result = max(result,bfs(check))
print(result)