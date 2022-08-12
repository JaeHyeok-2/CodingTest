n,m = map(int,input().split())
answer = []
visited = [False] *(n+1) # 같은 숫자 중복 제외를 위한 방문여부 배열

def dfs(start,count) :
    if count ==0 :
        print(" ".join(map(str,answer)))
        return
    for i in range(start,n+1) :
        if not visited[i]:
            answer.append(i)    #배열에 값을 넣은후,
            visited[i] = True   # 방문처리 한다
            dfs(start,count-1)  # 백트래킹을 한후, 현재 배열 첫번째 값에 대한 모든 경우의 수를 백트래킹
            answer.pop()        # 해당 값을 뺀후
            visited[i] = False  # False 처리

dfs(1,m)

