# 최소비용 = edges-> 크루스칼 알고리즘
import sys
input= sys.stdin.readline

def calDistance(p,q) :
    x1,y1 = p
    x2,y2=  q
    return (abs(x1-x2)**2 + abs(y1-y2) **2)**0.5

def getParent(parent,x) :
    if parent[x] != x :
        parent[x] = getParent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b) :
    a = getParent(parent,a)
    b = getParent(parent,b)

    if a > b :
        parent[a] = b
    else :
        parent[b] = a

n = int(input())
parent = [i for i in range(n)]
edges = []
stars = []

for _ in range(n) :
    x,y = map(float,input().split())
    stars.append((x,y))
# 0,1,2 ->
for i in range(n) :
    for j in range(i+1,n) :
        dist =calDistance(stars[i],stars[j])
        edges.append((dist,i,j))

edges.sort()

result = 0
for edge in edges :
    distance,i,j = edge
    if getParent(parent,i) == getParent(parent,j) :
        continue
    union_parent(parent,i,j)
    result += float(distance)

print(result)
