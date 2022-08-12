import sys
input= sys.stdin.readline

def getParent(parent,x) :
    if parent[x] != x :
        parent[x] = getParent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b) :
    a = getParent(parent,a)
    b = getParent(parent,b)
    if a== b:
        return
    if a > b :
        parent[a] = b
    else :
        parent[b] = a


n,m = map(int,input().split())
board = [list(input().strip()) for _ in range(n)]
parent = [i for i in range(n *m)]

direction = dict()
direction['D'] = [1,0]
direction['U'] = [-1,0]
direction['R'] = [0,1]
direction['L'] = [0,-1]

for i in range(n*m) :
    r = i//m
    c = i% m
    current = board[r][c] # 다음으로 가야할 방향이 적혀있는값

    nr = r + direction[current][0]
    nc = c + direction[current][1]

    j = nr *m + nc
    if j < 0 or j >= n*m : continue
    union_parent(parent,i,j)

answer = 0

visited = dict()


for i in range(n*m) :
    if getParent(parent,i) not in visited :
        answer += 1
        visited[parent[i]] = True

print(answer)