from collections import deque
import copy

n = int(input())
indegree = []*(n+1)     #차수를 담을 배열
graph = [[] for _ in range(n+1)]    #각 수강신청 연결리스트 생성
time = [0]*(n+1)    #수강과목당 수강시간

for i in range(1,n+1) :
    info = list(map(int,input()))
    time[i] = info[0]
    for x in info[1:-1]:
        indegree[i]+=1
        graph[x].append(i)  #선수강이 필요한 과목 x에  선수강과목 i를 삽입

def topology_sort() :
    result = copy.deepcopy(time)    #result 의 초기값은 time으로 설정 -> 만약 어떤과목도 선수강과목이 없다면, result가 답이므로.
    q = deque()

    while q:
        now = q.popleft()
        for i in graph[now] :
            result[i] = max(result[i],result[now] + time[i])    #이전의 저장했던 값 < 현재 탐색을 통한 총계산값 이어야함 ex) result[1] = 40이였는데 , result[0] = 30 time[1] = 40 이라면 result[1]은 70이 되어야함
            indegree[i] -=1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1,n+1):
        print(result[i])
topology_sort()

