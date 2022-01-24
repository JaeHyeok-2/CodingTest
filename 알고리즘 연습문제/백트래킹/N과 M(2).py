# https://www.acmicpc.net/problem/15650
"""
백트래킹없이 순열로 푸는 방식
from itertools import combinations

n,m = map(int,input().split())
lst = [i for i in range(1,n+1)]
candidates = list(combinations(lst,m))

for candidate in candidates :
  for i in candidate :
    print(i,end = ' ')
  print()

"""

n,m = map(int,input().split())
answer = []
visited = [False] *(n+1)
def dfs(start,count) :
    if count == 0 :
        print(" ".join(map(str,answer)))
        return
    for i in range(start,n+1) :
        if not visited[i] :
            answer.append(i)
            visited[i] = True
            dfs(i,count-1)
            answer.pop()
            visited[i] = False
dfs(1,m)