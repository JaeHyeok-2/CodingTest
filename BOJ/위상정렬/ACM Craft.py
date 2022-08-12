# https://www.acmicpc.net/problem/1005

import sys
import copy
from collections import deque
input = sys.stdin.readline

def topology_sort(time,indegree,end) :
    result = copy.deepcopy(time)
    q = deque()
    for i in range(1,n+1) :
        if indegree[i] == 0 :
            q.append((i))

    while q :
        now = q.popleft()
        for next in graph[now] :
            result[next] = max(result[next], result[now] + time[next])
            indegree[next] -=1
            if indegree[next] == 0 :
                q.append((next))

    print(result[end])


for _ in range(int(input())) :
    n,k = map(int,input().split()) #n : 건물의 개수 , k : 건물의 규칙  k줄입력받는다.
    indegree = [0] * (n+1)
    time = [0] + list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]
    # 건물 순서 입력
    for i in range(k) :
        a,b = map(int,input().split())
        graph[a].append(b)
        indegree[b] +=1
    end = int(input())
    topology_sort(time,indegree,end)



