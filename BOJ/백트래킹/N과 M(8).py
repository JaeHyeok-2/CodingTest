n, m = map(int, input().split())
number = list(map(int, input().split()))
number.sort()
visited = [False] * n
answer = []

def dfs(start, count):
    if count == 0:
        print(" ".join(map(str, answer)))
        return

    for i in range(start, n):
        answer.append(number[i])
        dfs(i, count - 1)
        answer.pop()


dfs(0, m)