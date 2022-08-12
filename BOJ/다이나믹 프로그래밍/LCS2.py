import sys
input =sys.stdin.readline
A = [0] + list(input().rstrip())
B = [0] + list(input().rstrip())

dp = [[""] * len(B) for _ in range(len(A))]

len_a = len(A)
len_b = len(B)

for i in range(1,len_a) :
  for j in range(1,len_b) :
    if A[i] == B[j] :
      dp[i][j] = dp[i-1][j-1] + A[i]
    else :
      if len(dp[i-1][j]) > len(dp[i][j-1]) :
        dp[i][j] = dp[i-1][j]
      else :
        dp[i][j] = dp[i][j-1]

print(len(dp[len_a-1][len_b-1]))
print(dp[len_a-1][len_b-1])
