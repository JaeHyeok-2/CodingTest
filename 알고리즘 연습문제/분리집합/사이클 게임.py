#  https://www.acmicpc.net/problem/20040
import sys
input =sys.stdin.readline

flag = False
def find_parent(parent,x) :
  if parent[x] != x :
    parent[x] = find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent,a,b) :
  global flag
  a = find_parent(parent,a)
  b = find_parent(parent,b)
  if a ==b :
    flag = True # 같을경우 Cycle 발생
    return
  elif a > b :
    parent[a] = b
  else :
    parent[b] = a

n,m = map(int,input().split())
parent = [i for i in range(n)]

answer = 0
for _ in range(m) :
  u,v = map(int,input().split())
  answer +=1

  union_parent(parent,u,v)
  if flag :
    break
if not flag :
  print(0)
else :
  print(answer)