# 1. DFS 방식으로 풀기
import sys
input =sys.stdin.readline
N = int(input())
data = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())

minimum =1e9
maximum=-1e9
def dfs(i,now):
    global add,sub,mul,div,minimum,maximum
    if(i == N) :
        minimum = min(minimum,now)
        maximum = max(maximum,now)
    else :
        if add >0 :
            add -=1
            dfs(i+1,now + data[i])
            add +=1
        if sub >0 :
            sub -=1
            dfs(i+1,now -data[i])
            sub +=1
        if mul > 0 :
            mul -=1
            dfs(i+1,now *data[i])
            mul+=1
        if div >0 :
            div -=1
            dfs(i+1,int(now/data[i]))
            div+=1

dfs(1,data[0])
print(maximum)
print(minimum)