import heapq
import sys
input =sys.stdin.readline

n,k = map(int,input().split())
gem = [list(map(int,input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]

gem.sort()
bag.sort()

storage = []
res = 0
for _ in range(k) :
    capacity = heapq.heappop(bag)
    #print(capacity)
    while gem and capacity >= gem[0][0]:
        value,weight = heapq.heappop(gem)
        heapq.heappush(storage,-weight)

    # storage에 보석이있다면, 가장높은거를 하나꺼내고,
    if storage :
        res -=heapq.heappop(storage)

    # gem 도 더이상없고, storage에도 보석이없다면 끝
    elif not gem :
        break
print(res)