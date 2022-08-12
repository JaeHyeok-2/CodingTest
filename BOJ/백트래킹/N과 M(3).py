n,m = map(int,input().split())
answer = []
#visited = [False] *(n+1)
def dfs(start,count) :
    if count == 0 :
        print(" ".join(map(str,answer)))
        return
    for i in range(start,n+1) :
        answer.append(i)
        dfs(start,count-1)  #중복을 허용하므로 start 를 인자로 넣어준다.
        answer.pop()
dfs(1,m)