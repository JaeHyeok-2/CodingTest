n,m = map(int,input().split())
number = list(map(int,input().split()))
number.sort()
answer = []
def dfs(start,n,m) :
    if m == 0 :
        print(" ".join(map(str,answer)))
        return
    before = 0
    for i in range(start,n) :
        if before != number[i]:
            answer.append(number[i])
            before = number[i]
            dfs(i,n,m-1)
            answer.pop()

dfs(0,n,m)

