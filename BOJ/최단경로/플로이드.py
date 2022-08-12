n = int(input())
m = int(input())
INF = 1e9
graph = [[] for _ in range(n+1)]
distance= [[INF] *(n+1) for _ in range(n+1)]
for i in range(n+1):
  for j in range(n+1):
    if i==j :
      distance[i][j] =0

for _ in range(m):
  a,b,cost = map(int,input().split())
  if distance[a][b] > cost: #여기를 꼭써야함
    distance[a][b] = cost

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      distance[i][j] = min(distance[i][j],distance[i][k]+distance[k][j])

for i in range(1,n+1):
  for j in range(1,n+1):
    if distance[i][j] ==INF:
      print(0,end = ' ')
    else :
      print(distance[i][j],end = ' ')
  print()