n,m = map(int,input().split())
number = list(map(int,input().split()))
number.sort()
answer = []

def dfs(start,n,m) :
    if m== 0 :
        print(" ".join(map(str,answer)))
        return
    before = 0 # 1,4,7,7,7,9,9에서  첫번째 7에 대해서 수행하면, 다음 7,7은 수행할 필요가없다.
    for i in range(n):
        if before != number[i] :
            before = number[i]
            answer.append(number[i])
            dfs(start,n,m-1)
            answer.pop()

dfs(0,n,m)