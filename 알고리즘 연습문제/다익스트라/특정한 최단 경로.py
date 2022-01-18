"""
https://www.acmicpc.net/problem/1504

문제 설명
 # 방향성 그래프가 주어질때, 1번에서 N번까지의 정점까지 최단거리로 이동
 # 단, 2개의 정점을 반드시 지나야 하는 조건이 주어진다
 # 지날 수 있다면 ,그때의 최솟값, 없다면 -1을 출력
 한 지점에서 다른 지점까지의 최솟값을 구하는 문제 : 다익스트라(힙)
"""
import sys
import heapq
input = sys.stdin.readline
INF =int(1e9)
n,m = map(int,input().split()) # n : 정점의 수 m : 간선의 수
graph = [[] for _ in range(n+1)] # 1~n번까지의 그래프 연결리스트
distance= [INF] *(n+1) # 한지점부터 다른지점까지의 거리를 저장할 배열

for _ in range(m):
    a,b,cost = map(int,input().split()) # 정점 a 에서 정점 b 까지의 거리
    # 양방향 노드이므로 둘다 연결
    graph[a].append((b,cost))
    graph[b].append((a,cost))

#경유지 2개 via
v1,v2 = map(int,input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) # 거리,정점순으로 입력
    distance[start] = 0 # 자기자신과의 거리는 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for nextNode in graph[now]:
            cost = dist + nextNode[1]
            next = nextNode[0]
            if distance[next] > cost :
                distance[next] = cost
                heapq.heappush(q,(cost,next))

    """
        문제에서 반드시 v1,v2를 경유해야하므로, 2가지 경로를 생각했음
        1번 -> v1 ->v2 ->N번
        1번 -> v2 ->v1 ->N번 
        둘중의 값중 최소값을 구하면됌
    """
    
dijkstra(1)
# 1번에서 v1,v2까지의 거리를 저장한다
destination_v1 = distance[v1]
destination_v2 = distance[v2]

# 거리 배열을 다시 초기화 시켜준다
distance = [INF] *(n+1)

# 이제 v1에서 다익스트라 함수를 통해 모든 노드의 길이를 살펴보면
# v1에서 v2 , N까지의 거리를 각각 저장한다.

dijkstra(v1)
destination_v1_N = distance[n]
destination_v1_v2 = distance[v2]

# 거리 배열을 다시 초기화 시켜준다
distance = [INF] *(n+1)

#이번에는 v2에서 v1과 N번까지의 거리를 살펴보면
dijkstra(v2)
destination_v2_N = distance[n]
destination_v2_v1 = distance[v1]

# 1번 -> v1 -> v2 -> N
# 1번 -> v2 -> v1 -> N 중의 최소값구하기
result = min(destination_v1 + destination_v1_v2 + destination_v2_N, destination_v2 + destination_v2_v1 + destination_v1_N)

if result >= 1e9 : # 갈수 없다면
    print('-1')
else :
    print(result)