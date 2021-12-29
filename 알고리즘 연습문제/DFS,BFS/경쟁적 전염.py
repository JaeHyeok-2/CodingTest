# https://www.acmicpc.net/problem/18405
from collections import deque
n,k = map(int,input().split())
graph = []
data = []

for i in range(n):
  graph.append(list(map(int,input().split())))
  for j in range(n):
    if graph[i][j] != 0:
      data.append((graph[i][j],0,i,j))

data.sort() # 바이러스 순으로 정렬
q = deque(data) #큐에 배열 삽입

time,fr,fc = map(int,input().split())

dr = [1,0,-1,0]
dc = [0,1,0,-1]

while q :
  virus,s,r,c = q.popleft()
  if s == time :
    break
  for i in range(4) :
    nr = r + dr[i]
    nc = c + dc[i]
    if nr>=0 and nc>=0 and nr<n and nc<n :
      if(graph[nr][nc] == 0) :
        graph[nr][nc] = virus
        q.append((virus,s+1,nr,nc))

print(graph[fr-1][fc-1])