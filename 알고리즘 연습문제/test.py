import sys
import heapq
input= sys.stdin.readline
n = int(input())

office = []
for i in range(n) :
    start ,end = map(int,input().split())
    office.append((start,end))
office.sort(key =lambda x : (x[1],x[0]))
#print(office)

prev =0
cnt = 0
for i in range(n) :
    if prev <= office[i][0] :
        prev = office[i][1]
        cnt +=1

print(cnt)
