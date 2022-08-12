# https://www.acmicpc.net/problem/1806
import sys
input= sys.stdin.readline

n,s = map(int,input().split())
arr = list(map(int,input().split()))

interval_sum = 0
end = 0
length = int(1e9)

temp = 0
for start in range(n) :
    while interval_sum < s and end < n :
        interval_sum += arr[end]
        end+=1
        temp +=1

    if interval_sum >= s :
        length = min(length,temp)
    interval_sum -=arr[start]
    temp -=1

if length == int(1e9) :
    print(0)
else :
    print(length)