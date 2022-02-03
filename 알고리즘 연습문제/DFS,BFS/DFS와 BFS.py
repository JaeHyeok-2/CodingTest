from collections import deque
from sys import stdin

input = stdin.readline

n, m, v = map(int, input().split())
visited = [False] * (n + 1)
board = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)
for i in range(1,n+1):
    board[i].sort()
#print(board)
def dfs(start) :
    if visited[start] :
        return
    visited[start] = True
    print(start,end = " ")
    for next in board[start] :
        if not visited[next] :
            dfs(next)


def bfs(start):
    queue = deque([start])
    visited[start] = True


    while queue:
        now = queue.popleft()
        for next in board[now]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
        print(now, end=" ")

dfs(v)
visited = [False] *(n+1)
print()
bfs(v)