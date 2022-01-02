# 2,3,5 만을 소인수로 가지는 수 : 못생긴 수라고 한다.
# 1도 못생긴 수로 표현
# 1,2,3,4,5,6,8,9,10,12,14,1
n= int(input())
dp = [0]*(n+1)
i2 =i3 = i5 = 0
next2 =2
next3 =3
next5 =5

dp[0] =1
for i in range(1,n):
    dp[i] = min(next2,next3,next5)
    if dp[i] == next2:
        i2+=1
        next2 = dp[i2]*2
    if dp[i] == next3:
        i3+=1
        next3 = dp[i3]*3
    if dp[i] == next5:
        i5+=1
        next5 = dp[i5]*5
print(max(dp))