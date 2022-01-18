# https://www.acmicpc.net/problem/1149

import sys
input = sys.stdin.readline
n = int(input())
color =[list(map(int,input().split())) for _ in range(n)] # 각줄을 입력으로 2차원 배열 생성

for i in range(1,n): # 각 칸마다의 최소값 구하기
    color[i][0] = color[i][0] + min(color[i-1][1],color[i-1][2])
    color[i][1] = color[i][1] + min(color[i-1][0],color[i-1][2])
    color[i][2] = color[i][2] + min(color[i-1][0],color[i-1][1])

print(min(color[n-1]))