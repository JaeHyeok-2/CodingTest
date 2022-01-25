n, m = map(int, input().split())
number = list(map(int, input().split()))
number.sort()
answer = []

def dfs(count):
    if count == 0:
        print(" ".join(map(str, answer)))
        return

    for i in range(n):
        answer.append(number[i])
        dfs(count - 1)

        answer.pop()
dfs(m)