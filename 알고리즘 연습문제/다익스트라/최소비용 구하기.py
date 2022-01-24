import sys
import heapq
input =sys.stdin.readline
# 도시 개수
n = int(input())
# 버스 개수
m = int(input())
# 버스 노선을 담을 노드
graph = [[] for _ in range(n+1)]
INF = 1e9
distance = [INF] *(n+1)
for _ in range(m) :
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))

start,end = map(int,input().split())

def dijkstra(start) :
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for next in graph[now] :
            cost = dist + next[1]
            nextNode = next[0]
            if distance[nextNode] > cost :
                distance[nextNode] = cost
                heapq.heappush(q,(cost,nextNode))
dijkstra(start)
print(distance[end])

