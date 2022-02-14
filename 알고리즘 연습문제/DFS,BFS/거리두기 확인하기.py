# https://programmers.co.kr/learn/courses/30/lessons/81302


from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def check(candidates, board):
    for candidate in candidates:
        # 본인 기준 2칸내까지만 탐색하면되지않나?
        visited = [[0] * 5 for _ in range(5)]
        x, y = candidate
        visited[x][y] = 1
        q = deque([(x, y, 0)])
        while q:
            x, y, cnt = q.popleft()
            if cnt == 2:
                break

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                    if board[nx][ny] == 'O':
                        visited[nx][ny] = 1
                        q.append((nx, ny, cnt + 1))
                    if board[nx][ny] == 'P':
                        return False
    return True


def solution(places):
    answer = []

    for place in places:
        board = [[''] * 5 for _ in range(5)]
        candidates = []
        for i in range(5):
            data = place[i]
            # print(data)
            for j in range(5):
                board[i][j] = data[j]
                if board[i][j] == 'P': candidates.append((i, j))

        #
        flag = check(candidates, board)
        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer