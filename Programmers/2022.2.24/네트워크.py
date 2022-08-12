def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def solution(n, computers):
    answer = 0
    parent = [i for i in range(n)]

    for i in range(n):
        computer = computers[i]
        for j in range(n):
            if i == j:
                continue
            if computer[j] == 1:
                union_parent(parent, i, j)

    cnt = set()

    for i in range(n):
        parent[i] = find_parent(parent, i)
        cnt.add(parent[i])

    return len(cnt)