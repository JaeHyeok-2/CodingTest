import sys
input= sys.stdin.readline

n,s = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
def backTracking(idx,value) :
    global cnt
    if idx >=n :
        return
    value +=arr[idx]

    if value == s :
        cnt +=1

    backTracking(idx+1,value)
    backTracking(idx+1,value-arr[idx])
backTracking(0,0)
print(cnt)
