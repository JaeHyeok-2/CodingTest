# https://www.acmicpc.net/problem/1197

"""
최소 스패닝 트리 : 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리 ( union-parent 사용 )
"""
import sys
input = sys.stdin.readline

def find_parent(parent,x) :
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b ) :
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a > b :
        parent[a] = b
    else :
        parent[b] = a

v,e = map(int,input().split())
edges = []
parent= [i for i in range(v+1)]

for _ in range(e) :
    a,b,c = map(int,input().split())
    edges.append((c,a,b))

edges.sort() # 아래랑 같음
#edges.sort(key = lambda x : x[0]) # c에 대해서 오름차순 정렬

res = 0
for edge in edges :
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b) :
        union_parent(parent,a,b)
        res += cost
print(res)