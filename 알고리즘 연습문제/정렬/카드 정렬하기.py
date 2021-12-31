# https://www.acmicpc.net/problem/1715
# 최소 힙을 이용한 그리디 알고리즘
import heapq
n= int(input())
heap = []
for _ in range(n):
    data = int(input())
    heapq.heappush(heap,data) # 최소값 순서대로

total = 0 # 결과값
# heap 에 원소가 1개가 남을때까지 반복 = 1개가남았다는것은 모두 섞였다는의미
while len(heap) != 1 :
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    total +=(a+b) # 카드섞은 회수를 결과값에 저장한후,
    heapq.heappush(heap,(a+b)) # 카드를 섞은후, 힙에 다시 저장
print(total) # 결과 출력