n, m = map(int, input().split())
answer = []
def dfs(start, count):
    if count == 0:
        print(" ".join(map(str, answer)))
        return

    for i in range(start, n + 1):
        answer.append(i)
        dfs(i, count - 1)
        answer.pop()

dfs(1, m)