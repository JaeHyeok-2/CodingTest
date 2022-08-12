n = int(input())
t,p = [],[]

for i in range(n) :
    a,b = map(int,input().split()) # a,b = 상담걸리는날짜, 돈
    t.append(a)
    p.append(b)

dp = [0] *(n+1)

max_value = 0
for i in range(n-1,-1,-1) :
    time = i + t[i] # 오늘날짜
    if time >n :
        dp[i] = max_value
    elif time<=n :
        dp[i] = max(p[i] + dp[time],max_value)
        max_value = dp[i]

print(max_value)
