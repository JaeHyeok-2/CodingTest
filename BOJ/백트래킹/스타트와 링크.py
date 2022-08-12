import sys
from collections import deque
from itertools import combinations
import copy
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
result = int(1e9)
team = [i for i in range(n)]
q = deque()
visited = [False] * n


def backTracking(start,count) :
    global result
    if count == n//2 :
        temp = Sum(q)
        result = min(temp,result)
        return
    for i in range(start,n) :
        if not visited[i] :
            q.append(i)
            visited[i] = True
            backTracking(i,count+1)
            q.popleft()
            visited[i]= False

def Sum(queue) :
    q = copy.deepcopy(queue)
    start = []
    while q :
        start.append(q.popleft())
    link = list(set(team) - set(start))
    print(start)
    a,b = [0] *2
    for i in combinations(start,2):
        a +=board[i[0]][i[1]]
        a +=board[i[1]][i[0]]

    for i in combinations(link,2):
        b +=board[i[0]][i[1]]
        b +=board[i[0]][i[1]]
    return abs(a-b)


backTracking(0,0)
print(result)