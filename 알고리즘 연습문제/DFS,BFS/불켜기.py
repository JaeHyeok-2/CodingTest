from collections import defaultdict, deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    x_, y_, a, b = map(int, input().split())
    graph[(x_ - 1), (y_ - 1)].append((a - 1, b - 1))



dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
    visit = [[0] * n for _ in range(n)]
    light = [[0] * n for _ in range(n)]
    result = 1
    q = deque()
    q.append([0,0])
    visit[0][0] =1
    light[0][0] = 1
    while q:
        x, y = q.popleft()

        for tx, ty in graph[(x, y)]:
            if not light[tx][ty]:
                light[tx][ty] = 1
                result += 1

                for i in range(4):
                    nx = tx + dx[i]
                    ny = ty + dy[i]
                    if 0 <= nx < n and 0 <= ny < n :
                        if visit[nx][ny]:
                            q.append((nx, ny))


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if light[nx][ny] and not visit[nx][ny]:
                    q.append((nx, ny))
                    visit[nx][ny] = 1
    return result


result = bfs()
print(result)
