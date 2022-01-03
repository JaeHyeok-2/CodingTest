import heapq
n,m = map(int,input().split())
INF =int(1e9)
distance = [INF] * (n+1)
distance[0] = -1
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dijkstra(start) :
    distance[start] = 0
    q = [(0,start)]
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for next_node in graph[now] :
            cost =1 + distance[now]
            if distance[next_node] > cost :
                distance[next_node] = cost
                heapq.heappush(q,(cost,next_node))

dijkstra(1)
maximum = max(distance)
count = distance.count(maximum)
index = distance.index(maximum)
print(index,maximum,count, sep= " ")


