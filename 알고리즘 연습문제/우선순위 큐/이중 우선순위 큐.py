#https://www.acmicpc.net/problem/7662
import heapq
import sys
input = sys.stdin.readline
result = []
for tc in range(int(input())) :
    visited = [False] *1_000_001

    n = int(input()) # 횟수
    minq,maxq = [],[]
    for i in range(n):
        oper,number = input().split()

        if oper == 'I' :
            heapq.heappush(minq,(int(number),i))
            heapq.heappush(maxq,(-int(number),i))
            visited[i] = True
        elif number == '1':
            while maxq and not visited[maxq[0][1]] :
                heapq.heappop(maxq)
            if maxq :
                visited[maxq[0][1]] = False
                heapq.heappop(maxq)
        else :
            while minq and not visited[minq[0][1]] :
                heapq.heappop(minq)
            if minq:
                visited[minq[0][1]] = False
                heapq.heappop(minq)
    while minq and not visited[minq[0][1]]:
        heapq.heappop(minq)
    while maxq and not visited[maxq[0][1]] :
        heapq.heappop(maxq)
    result.append("{} {}".format(-maxq[0][0],minq[0][0]) if maxq and minq else 'EMPTY')
print('\n'.join(result))
