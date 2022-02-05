"""
 # 제약조건
 # left 숫자가 right보다 클 경우 : left카드만 버리거나  둘다버리기 ; right카드만 버리기   (right만 버릴시 획득, 그외는 획득 x )
 # left가 right보다 작을경우 : left 카드만 버리거나 둘다버리기 ; 점수확득 불가


"""

n = int(input()) #카드 수
left = list(map(int,input().split()))
right = list(map(int,input().split()))

dp = [[0] *(n+1) for _ in range(n+1)] # 마진값은 0 으로 채우기위해서

#row,col = left ,right 로 하자

for i in range(n-1,-1,-1) :
    for j in range(n-1,-1,-1) :
        if right[j] < left[i] :
            #왼쪽만 버릴때, 둘다 버릴때 , 오른쪽만 버리고 값 추가
            dp[i][j] = max(dp[i+1][j],dp[i+1][j+1],dp[i][j+1] + right[j])
        else :
            dp[i][j] = max(dp[i+1][j],dp[i+1][j+1])
print(dp[0][0])