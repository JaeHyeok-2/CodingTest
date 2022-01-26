#https://www.acmicpc.net/problem/2003

n,m = map(int,input().split())
data = list(map(int,input().split()))

interval_sum = 0
count = 0
end = 0
for start in range(n) :
    while interval_sum <m and end < n :
        interval_sum += data[end]
        end+=1

    if interval_sum == m :
        count+=1
    interval_sum -=data[start]
print(count)