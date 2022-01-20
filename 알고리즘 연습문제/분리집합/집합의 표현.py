# https://www.acmicpc.net/problem/1717
import sys
sys.setrecursionlimit(100000)
input= sys.stdin.readline

n,m = map(int,input().split())
parent = [0]*(n+1)
for i in range(n+1):
    parent[i] = i

def find_parent(x) :
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a==b :
        return
    if a > b :
        parent[a] = b
    else :
        parent[b] = a

for _ in range(m) :
    oper,a,b = map(int,input().split())
    if oper == 0 :
        union_parent(a,b)
    else :
        if find_parent(a) == find_parent(b) :
            print('YES')
        else:
            print('NO')