"""
""연속적인  장이므로!!!! 1,2,3,4,5장이있을때, 1,5장을 합치면안됌!!!!
Heap을 사용했다가 틀림
"""
import sys
input= sys.stdin.readline

for _ in range(int(input())) :
    n = int(input())
    arr = list(map(int,input().split()))
    dp = [0] *(n+1)
    # 정렬하면안됌. 소설에는 순서가 있기때문
    dp[0] = arr[0] # 첫 페이지
