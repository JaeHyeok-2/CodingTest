# https://www.acmicpc.net/problem/1766
import heapq
import sys
input= sys.stdin.readline

n,m = map(int,input().split()) # n : 문제 개수 , m : 선행문제에 대한 정보 개수
indegree = [0] *(n+1) # 1~n 이편하므로
visited = [False] *(n+1)
graph = [[] for _ in range(n+1)]

heap = []
for i in range(m) :
    a,b = map(int,input().split()) # a를 풀고 b를 푸는 방식 a->b
    indegree[b] +=1
    graph[a].append(b)


for i in range(1,n+1) :
    graph[i].sort()

#print(graph)

answer = []
def topology_sort() :
    for i in range(1,n+1) :
        if indegree[i] == 0 :
            heapq.heappush(heap,i)
    while heap :
        now = heapq.heappop(heap)
        answer.append(now)
        visited[now] = True
        for next in graph[now] :
            indegree[next] -=1
            if indegree[next] == 0 :
                heapq.heappush(heap,next)
                visited[next] = True
                # (3,1) ,(4,2)에 대해 실행한다고 해보자
                # heap =[3,4] 가 입력되어있을것이고
    for i in range(1,n+1) :
        if not visited[i] :
            answer.append(i)

topology_sort()

for i in answer :
    print(i,end = ' ')