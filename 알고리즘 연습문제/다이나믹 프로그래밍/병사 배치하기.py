n = int(input())
array = list(map(int,input().split()))

dp = [1]*(n+1)
array.reverse() # 순서를 뒤집어서 오름차순으로 구하기
for i in range(1,n):
    for j in range(0,i):
        if array[i] > array[j] :
            dp[i] = max(dp[i],dp[j]+1)
print(n - max(dp))