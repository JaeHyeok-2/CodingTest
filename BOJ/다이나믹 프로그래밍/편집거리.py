"""
 # Insert, Remove , Replace 3개를 이용하여, 문자열 A ->B로 만들기

[str1][str2]
       s a t u r d a y
     0 1 2 3 4 5 6 7 8
  s  1 0 1 2 3 4 5 6 7
  u  2 1 1 2 2 3 4 5 6
  n  3 2 2 2 3 3 4 5 6
  d  4 3 3 3 3 4 3 4 5
  a  5 4 3 4 4 4 4 3 5
  y  6 5 4 4 5 5 5 5 3

"""
def edit_dist(str1,str2):
    n = len(str1)
    m = len(str2)
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1,n+1):
        dp[i][0] = i
    for j in range(1,m+1):
        dp[0][j] = j

    for i in range(1,n+1):
        for j in range(1,m+1):
            if str1[i-1] == str2[j-1] :
                dp[i][j] = dp[i-1][j-1]
            else :
                dp[i][j] = 1 + min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
    return dp[n][m]

str1 = input()
str2 = input()
edit_dist(str1,str2)