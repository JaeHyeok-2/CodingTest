import sys

def find_parent(parent,x) :
  if parent[x] != x :
    parent[x] = find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b) :
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a > b :
    parent[a] =b
  else :
    parent[b] = a


input = sys.stdin.readline
n,m =map(int,input().split())
parent = [0] *n
edges = []

for i in range(n):
  parent[i] = i

total = 0 #총 설치시 금액
for _ in range(m) :
  a,b,dist = map(int,input().split())
  edges.append((dist,a,b))
  total +=dist

edges.sort() # 비용이 저렴한 순으로 정렬 (비용,a,b) 저장

result = 0 # 최소한의 설치시 금액
for edge in edges:
  cost,a,b = edge
  if find_parent(parent,a) != find_parent(parent,b):
    union_parent(parent,a,b)
    result +=cost

print(total -result)
"""
테스트 케이스

7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11

"""