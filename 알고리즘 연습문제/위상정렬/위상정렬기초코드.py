#방향 그래프의 모든 노드를 "방향성에 거스르지 않도록 순서대로 나열 하는것" ex) 수강신청할때
# queue 를 사용한다
from collections import deque
v,e = map(int,input().split())  #정점과 간선의 개수
indegree = [0]*(v+1)    #진입차수 배열로 선언
graph = [[] for _ in range(v+1)]    #연결 리스트 선언

for _ in range(e) :
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1  #a->b이므로 b의 진입차수를 증가

def topology_sort():
    result = []
    q = deque()
    #진입차수가 0인것부터 시작
    for i in range(1,v+1) :
        if indegree[i] == 0 :
            q.append(i)
    # 큐가 빌때까지
    while q :
        now = q.popleft()
        result.append(now)
        for i in graph[now] :
            indegree[i] -=1
            if indegree[i] == 0:
                q.append(i)

    for i in result :
        print(i, end = ' ')
topology_sort()