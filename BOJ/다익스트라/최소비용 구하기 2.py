import sys
import heapq
input = sys.stdin.readline
n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

graph = [[] for _ in range(n+1)]

for _ in range(m) :
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))

start,end = map(int,input().split())


INF = int(1e9)
distance = [[INF,0] for _ in range(n+1)] # 첫번째 인자 : 해당 도시까지의 거리 , 두번째인자 : 현재 도시의 부모 도시

def dijkstra(start) :
    q = []
    heapq.heappush(q,(0,start))
    distance[start][0] = 0
    distance[start][1] = start

    while q :
        dist,now = heapq.heappop(q)
        if dist > distance[now][0] :
            continue

        for next in graph[now] :
            cost = dist + next[1]
            nextNode= next[0] # 연결된 버스
            if cost < distance[nextNode][0] :
                distance[nextNode][0] = cost

                distance[nextNode][1] = now
                heapq.heappush(q,(cost,nextNode))

dijkstra(start)

print(distance[end][0])
back = [end]
cnt = 1
while True :
   now = distance[end][1]
   end = now
   cnt +=1
   if end == start : break
   back.append(now)
back.append(start)

print(cnt)
for i in back[::-1] :
    print(i,end = ' ')


