import sys
from collections import deque
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    indegree = [0] * (n + 1)
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    data = list(map(int, input().split()))

    for i in range(n):
        for j in range(i + 1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())  # a ,b팀의 등수가 바뀌었다
        if graph[a][b]: # a가 등수가 더높았었다면 ?
            graph[a][b] = False  # b->a 이므로 , False
            graph[b][a] = True   # a가 b보다 높으므로 True
            indegree[a] += 1     # a가 등수가 낮아졌으므로 ,b->a를 가르킬예정 차수 1 추가
            indegree[b] -= 1     # a->b를 가르키던것이 없어지므로 1을뺀다

        else:   #b가 더높았었을경우, 즉 b>a에서 a>b가 될경우
            graph[a][b] = True   # a의 등수가 b보다 높으므로 ,
            graph[b][a] = False  # b는 등수가 a보다 낮아졌으므로
            indegree[b] += 1     # b가 낮아져서 a를 가르켜야함
            indegree[a] -= 1     # a가 b보다 등수가 좋아져서 b가 a를 가르키는상황

    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:     #처음 1등을 먼저 뺀다.
            q.append(i)

    certain = True   # q에 2개가들어가면, 중복등수가 존재하므로 flag
    cycle = False    # cycle이 존재한다면 q의 크기가 0 이되므로 flag 1개 생성

    for i in range(n):   # 노드의 개수만큼 탐색 -> 하나씩 커질때마다 값이 1개씩 나와야하므로.
        if len(q) == 0:
            cycle = True
            break

        if len(q) >= 2:
            certain = False
            break

        now = q.popleft()
        result.append(now)
        for j in range(1, n + 1):
            if graph[now][j]: # 현재 노드가 가르키고 있는 노드들
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=' ')
        print()