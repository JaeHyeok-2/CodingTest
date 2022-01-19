# https://www.acmicpc.net/problem/1717
import sys
sys.setrecursionlimit(10**6)
input= sys.stdin.readline

n,m = map(int,input().split())
parent = [i for i in range(0,n+1)]

def find_parent(parent,x) :
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b :
        parent[a] = b
    else :
        parent[b] = a

for _ in range(m) :
    oper,a,b = map(int,input().split())
    if oper == 0 :
        union_parent(parent,a,b)
    else :
        if find_parent(parent,a) == find_parent(parent,b) :
            print('YES')
        else:
            print('NO')