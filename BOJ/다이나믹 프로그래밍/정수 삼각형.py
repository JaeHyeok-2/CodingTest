#https://www.acmicpc.net/problem/1932 정수삼각형
"""
        7
      3   8
     8  1  0
    2  7  4  4
   4  5  2  6  5

    # 맨밑의 좌표부터 최대값을 갱신하면서 위로 올라가는 방식으로 하면,
"""
import sys
input = sys.stdin.readline
n = int(input()) # 삼각형 크기
dp = []

for i in range(n) :
  dp.append(list(map(int,input().split())))

for i in range(n-2,-1,-1):  #바닥의 값은 초기값
  for j in range(len(dp[i])) :  # 각 배열마다 크기가 다르므로 dp[i]의 길이만큼 반복
      dp[i][j] = dp[i][j] + max(dp[i+1][j],dp[i+1][j+1])
print(dp[0][0])
