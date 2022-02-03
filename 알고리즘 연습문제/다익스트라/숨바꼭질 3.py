import heapq
import sys
input = sys.stdin.readline
inf = sys.maxsize

n,k = map(int,input().split())
board = [inf] *(100001)
heap = []

def dijkstra(n,k) :
    if k <=n : # 술래보다 뒤에가있으면, 뒤로간만큼 뺀다.
        print(n-k)
        return
    heapq.heappush(heap,[0,n]) # 거리에 대해 가중치를 정함
    while heap :
        weight,now = heapq.heappop(heap)
        for i in [now-1,now+1,now*2] :
            if 0<=i<=100000:
                if i == now*2 and board[i] == inf : #방문하지 않았고, 순간이동 거리라면,
                    board[i] = weight # 순간이동 거리는 앞선 거리와 같고,
                    heapq.heappush(heap,[weight,i])
                elif board[i] == inf : # 앞뒤 1칸일경우,
                    board[i] = weight+1  # +1로 가중치를 더해준다.
                    heapq.heappush(heap,[weight+1,i])

    print(board[k])
dijkstra(n,k)