# https://www.acmicpc.net/problem/2887

import sys
input =sys.stdin.readline

def find_parent(parent,x) :
    if parent[x] !=x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b) :
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b:
        parent[a] = b
    else :
        parent[b] = a

n= int(input())
parent = [0] *(n+1)
for i in range(1,n) :
    parent[i] =i

x = []
y = []
z = []
for i in range(n) :
    x1,y1,z1 = map(int,input().split())
    x.append((x1,i))
    y.append((y1,i))
    z.append((z1,i))
x.sort()
y.sort()
z.sort() # 길이,번호 순으로 저장되어있음

edges = []
for i in range(n-1) :
    edges.append((x[i+1][0]-x[i][0],x[i][1],x[i+1][1])) # i ->i+1로 가는거리는 edges[0]값이다.
    edges.append((y[i+1][0]-y[i][0],y[i][1],y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0],z[i][1],z[i+1][1]))

edges.sort() # 거리가 짧은 순으로 나열

result = 0
for edge in edges :
    dist,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b) :
        union_parent(parent,a,b)
        result +=dist

print(result)