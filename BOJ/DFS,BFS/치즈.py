from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # row : n  , col : m
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
edgePosition = [[0,0],[0, m - 1], [n - 1, 0], [n - 1, m - 1]] # 각 모서리 좌표

def innerCheck():  # 사방으로 둘러쌓인 대기 확인
    q = deque(edgePosition) # 모서리 마다 탐색을 통해, 치즈로 둘러쌓인 내부 찾기
    while q:
        r, c = q.popleft()  # 현재 탐색 노드
        visited[r][c] = True
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 모눈종이 내에 존재하고,
            if 0 <= nr < n and 0 <= nc < m:
                # 실내온도 공기이면서, 방문하지 않은 곳
                if board[nr][nc] == 0 and not visited[nr][nc]:
                    q.append([nr, nc])
                    visited[nr][nc] = True


def meltingCheese():
    for r in range(n):
        for c in range(m):
            if board[r][c] == 1: # 치즈인 곳에서,
                count = 0
                # 4방향 탐색 후에,
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < n and 0 <= nc < m and visited[nr][nc]:
                        count += 1 # 공기로 둘러쌓여있다면 +1
                # count가 2이상이면 치즈가 녹는다.
                if count >= 2:
                    board[r][c] = 0


def countCheese(board):
    sum_value = 0
    for i in range(n):
        sum_value += sum(board[i])
    if sum_value == 0:
        return True
    return False



# 치즈 녹는 시간
time = 0
while True:
    visited = [[False] * m for _ in range(n)]  # n x m 방문여부
    innerCheck()
    meltingCheese()
    time += 1
    if countCheese(board):
        break
print(time)