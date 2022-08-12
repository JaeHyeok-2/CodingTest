n, m = map(int, input().split())
number = list(map(int, input().split()))
visited = [False] * (n + 1)
number.sort() # 오름차순을 위해 작은수부터 백트래킹

answer = []


def dfs(start, count):
    if count == 0:
        print(" ".join(map(str, answer)))
        return

    for i in range(start, n):
        if not visited[i]:
            answer.append(number[i])
            visited[i] = True
            dfs(0, count - 1)
            answer.pop()
            visited[i] = False


dfs(0, m)

