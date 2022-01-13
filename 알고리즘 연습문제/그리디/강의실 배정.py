import heapq
n = int(input())
heap = []
q = []

for _ in range(n):
    start,end = map(int,input().split())
    heapq.heappush(heap,(start,end))

start,end = heapq.heappop(heap)
heapq.heappush(q,end)

while heap :
    start,end = heapq.heappop(heap)
    if q[0] <=start :
        heapq.heappop(q)
    heapq.heappush(q,end)
print(len(q))
