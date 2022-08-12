import sys
from collections import deque
input = sys.stdin.readline

n,l,r = map(int,input().split()) # n = testCase 개수 , l = 두나라의 인원차의 최소, r = 두나라의 인원차의 최대
graph = [] # 각 나라의 인원을 담을 2차원 리스트

for _ in range(n):
  graph.append(list(map(int,input().split())))

dx = [1,0,-1,0] # 4방향 탐색
dy = [0,1,0,-1]

def bfs(i,j):
  visit[i][j] = True # 현재 칸 방문처리
  q = deque()
  q.append([i,j])
  temp =[]  # 현재 탐색중인 국가와 연합인 국가들을 담는 배열
  temp.append([i,j])
  while q:
    x,y =q.popleft()
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<n and visit[nx][ny] == False :
        if l<= abs(graph[nx][ny]-graph[x][y]) <= r :
          q.append([nx,ny])
          temp.append([nx,ny])
          visit[nx][ny] = True
  return temp # 연합인 국가들의 배열 리턴

result = 0
while True :
  visit = [[False]*n for _ in range(n)] #매번 계속 초기화
  flag = False  # 만약 연합이 없다면, False를 반환 , 있다면 True
  for i in range(n) :
    for j in range(n) :
      if not visit[i][j] :
        temp = bfs(i,j)
        if len(temp) > 1:
          flag = True
          num = sum(graph[x][y] for x,y in temp)//len(temp)
          for x,y in temp:
            graph[x][y] = num
  if not flag :
    break
  result +=1
print(result)