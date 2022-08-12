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
maximum = max(distance) #최대 거리의 번호
count = distance.count(maximum)  #최대거리의 번호 개수
index = distance.index(maximum)  #제일 왼쪽의 인덱스
print(index,maximum,count, sep= " ")


