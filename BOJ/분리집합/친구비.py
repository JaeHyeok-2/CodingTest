from sys import stdin
input =stdin.readline

n,m,k = map(int,input().split()) # 친구 수 , 친구 관계 , 가지고있는 금액
arr= [0] + list(map(int,input().split()))

friend = [i for i in range(n+1)]

def find(x) :
    if friend[x] == x :
        return x
    else :
        if arr[friend[x]] > arr[x] :
            arr[friend[x]] = arr[x]
        else :
            arr[x] = arr[friend[x]]
        friend[x] = find(friend[x])
        return friend[x]

def union(a,b) :
    a = find(a)
    b = find(b)
    if arr[friend[a]] > arr[friend[b]] :
        arr[friend[a]] = arr[friend[b]]
    else :
        arr[friend[b]] = arr[friend[a]]

    if a > b :
        friend[a] = b
    else :
        friend[b] = a
for _ in range(m) :
    v,w = map(int,input().split())
    union(v,w)

tmp = set()
total = 0
for i in range(1,n+1) :
    now = find(i)
    if now in tmp:
        continue
    # 없다면?
    else :
        tmp.add(now)
        total +=arr[now]

if total <= k :
    print(total)
else :
    print('Oh no')


