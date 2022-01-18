import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
# n = 인원,마을 수  m = 데이터 수 , x = 파티가 열리는 장소의 노드 번호
n,m,x = map(int,input().split())

graph = [[] for _ in range(n+1)]
backhome = [INF]*(n+1) # 각 번호에서 집가는 거리를 담을 배열,
distance = [INF] *(n+1)

for _ in range(m) :
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))

# 파티가 열리는 장소 : x
def backhomeDistance(party) :
    backhome[party] = 0
    q = []
    heapq.heappush(q,(0,party))
    while q:
        dist,now = heapq.heappop(q)
        if backhome[now] < dist :
            continue
        for nextNode in graph[now] :
            cost = nextNode[1] + dist
            next = nextNode[0]
            if backhome[next] > cost:
                backhome[next] = cost
                heapq.heappush(q,(cost,next))

def dijkstra(start) :
    global result
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for next in graph[now] :
            cost = next[1] + dist
            nextNode = next[0]
            if distance[nextNode] > cost :
                distance[nextNode] = cost
                heapq.heappush(q,(cost,nextNode))
    #return distance[n] + backhome[start]



result = 0
backhomeDistance(x) # 파티가 끝난후 각자의 집까지의 거리를 담은 배열

for i in range(1,n+1):
    dijkstra(i)
    result = max(result,distance[x] + backhome[i])
    distance = [INF] *(n+1)
print(result)