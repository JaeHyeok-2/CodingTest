n, m = map(int, input().split())
number = list(map(int, input().split()))
visited = [False] * (n + 1)
answer = []
number.sort()  # 오름차순


def dfs(start, count):
    if count == 0:
        print(" ".join(map(str, answer)))
        return

    for i in range(start, n):
        if not visited[i]:
            answer.append(number[i])
            visited[i] = True
            dfs(i + 1, count - 1)
            answer.pop()
            visited[i] = False


dfs(0, m)