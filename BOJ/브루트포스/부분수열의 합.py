import sys
from itertools import combinations

n,s = map(int,input().split())
arr = list(map(int,input().split()))

ans = 0
total = sum(arr)
for i in range(n+1) :
    value = 0
    datas = combinations(arr,i)
    for data in datas :
        value = sum(data)
        if s == value :
            ans +=1

if s == 0 :
    ans -=1
print(ans)