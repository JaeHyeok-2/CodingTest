import sys
from collections import deque
input= sys.stdin.readline

n,m = map(int,input().split()) #n = 사다리수, m = 뱀의 개수

ladders = dict()
snake = dict()
board = [0] * 101
visited = [False] * 101

for _ in range(n) :
    x,y = map(int,input().split())
    ladders[x] = y

for _ in range(m) :
    x,y = map(int,input().split())
    snake[x] = y


def bfs() :
    q = deque([1])
    visited[1] = True
    while q:
        now = q.popleft()
        # 현재 위치에서 갈수 있는 칸수
        for move in range(1,7) :
            next = now + move
            if 0<next<=100 and not visited[next] :
                if next in ladders.keys() :
                    next = ladders[next]

                if next in snake.keys() :
                    next = snake[next]

                if not visited[next]:
                    q.append(next)
                    board[next] = board[now] + 1
                    visited[next] = True


bfs()
print(board[100])
