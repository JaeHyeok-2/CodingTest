import sys
input= sys.stdin.readline

def find_parent(parent,x) :
  if parent[x] != x :
    parent[x] = find_parent(parent,parent[x])
  return parent[x]
def union_parent(parent,a,b):
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a > b :
    parent[a] = b
  else:
    parent[b] = a

n,m = map(int,input().split())
parent = [0] *(n+1)

for i in range(1,n+1):
  parent[i] = i

for i in range(n) :
  data = list(map(int,input().split()))
  for j in range(n) :
    if data[j] ==1 :
      a = find_parent(parent,i+1)
      b = find_parent(parent,j+1)
      union_parent(parent,a,b)

trip = list(map(int,input().split()))

flag = False

for i in range(m-1) :
  if find_parent(parent,trip[i]) != find_parent(parent,trip[i+1]):
    flag = True
    break
if flag :
  print("NO")
else :
  print("YES")