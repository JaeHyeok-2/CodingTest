n, m = map(int, input().split())
number = list(map(int, input().split()))
number.sort()

visited = [False] * n
answer = []

def dfs(start, n, m):
    if m == 0:
        print(" ".join(map(str, answer)))
        return

    overlap = 0
    for i in range(n):
        if not visited[i] and overlap != number[i]:
            answer.append(number[i])
            visited[i] = True
            # 이전의 숫자와 중복되지 않도록 overlap 변수 선언
            overlap = number[i]
            dfs(start + 1, n, m - 1)
            answer.pop()
            visited[i] = False

dfs(0, n, m)

