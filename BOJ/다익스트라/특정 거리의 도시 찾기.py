# https://www.acmicpc.net/problem/18352
# 다익스트라, BFS
from collections import deque
import sys
input = sys.stdin.readline  # 입력줄을 많이 받으므로, 쓰지않으면 시간초과가 뜬다
n,m,k,x = map(int,input().split()) # n : 정점의 수 , m : 도로의 개수 , k = 거리정보 ,x : 시작점

graph= [[] for _ in range(n+1)]
distance = [-1] *(n+1)
for _ in range(m) :
  a,b = map(int,input().split())
  graph[a].append(b)

def dijkstra(start) :
  distance[start] = 0
  q = deque([start])
  while q :
    now = q.popleft()
    for next_node in graph[now] :
      if distance[next_node] == -1 :
        distance[next_node] = distance[now] +1
        q.append(next_node)

dijkstra(x)

check = False
for i in range(1,n+1) :
  if distance[i] == k :
    print(i)
    check = True
if not check :
  print(-1)