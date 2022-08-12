# https://www.acmicpc.net/problem/1753
# graph와 distance 배열을 따로 선언후, 다익스트라로 최단경로 찾기
import  heapq
import sys
input = sys.stdin.readline

v,e = map(int,input().split()) # 정점 ,간선 개수
INF = int(1e9)
graph = [[] for _ in range(v+1)]
distance = [INF] *(v+1)
start = int(input())

for _ in range(e) :
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))

def dijkstra(start) :
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))

    while q:
        dist,now = heapq.heappop(q)
        if(distance[now] < dist) :
            continue
        for next in graph[now] :
            cost = dist + next[1]
            if (distance[next[0]] > cost) :
                distance[next[0]] = cost
                heapq.heappush(q,(cost,next[0]))
dijkstra(start)

for i in range(1,v+1) :
    if distance[i]>=INF:
        print("INF")
    else :
        print(distance[i])