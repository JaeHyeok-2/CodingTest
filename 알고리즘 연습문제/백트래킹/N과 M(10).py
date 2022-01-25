n, m = map(int, input().split())
number = list(map(int, input().split()))
number.sort()

answer = []
visited = [False] * n


def dfs(start, n, m):
    if m == 0:
        print(" ".join(map(str, answer)))
        return

    flag = 0
    for i in range(start, n):
        if not visited[i] and flag != number[i]:
            answer.append(number[i])
            visited[i] = True
            flag = number[i]
            dfs(i + 1, n, m - 1)
            visited[i] = False
            answer.pop()


dfs(0, n, m)