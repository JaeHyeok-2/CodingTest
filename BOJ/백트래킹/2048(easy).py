# https://www.acmicpc.net/problem/12100

import sys
from copy import deepcopy
input= sys.stdin.readline

N = int(input())
result = 0
board = [list(map(int,input().split())) for _ in range(N)]

# 0 ~ n-1 까지 위에서 부터 채워야함
def move_up(board): # 블록 위로 이동
    for i in range(N): # 열
        p = 0 # 행의 가장 상단은 0
        x = 0
        for j in range(N): # 행
            if board[j][i] == 0: continue # 0이면 continue
            if x == 0: x = board[j][i] # x가 비어있으면 더해줄 블록이 없다는 것이므로 x를 변경
            else:
                if x == board[j][i]: # 지난 블록과 같은 경우
                    board[p][i] = x * 2 # 이동할 곳에 x * 2 값을 저장
                    x = 0 # 블록을 더했으므로 x 초기화
                    p += 1 # 행에서 갈 수 있는 가장 상단 행을 채웠으므로 다음 블록이 이동하게될 위치 증가
                else: # 지난 블록과 같지 않은 경우
                    board[p][i] = x # 이동할 곳에 지난 블록인 x값을 저장
                    x = board[j][i] # 이전 블록을 새로운 블록으로 변경
                    p += 1 # 행에서 갈 수 있는 가장 상단을 채웠으므로 다음 블록이 이동하게될 위치 증가
            board[j][i] = 0 # 블록 이동했으므로 비워줌
        if x != 0: board[p][i] = x # 행의 가장 하단까지 도달 후에 이동할 블록이 남아있으면 블록 이동
    return board

def move_down(board):
    for i in range(N): # 열
        p = N - 1 # 행의 가장 하단
        x = 0
        for j in range(N - 1, -1, -1): # 행
            if board[j][i] == 0: continue # 0이면 continue
            if x == 0: x = board[j][i] # x가 비어있으면 더해줄 이전 블록이 없다는 것이므로 x를 변경
            else:
                if x == board[j][i]: # 지난 블록과 같은 경우
                    board[p][i] = x * 2 # 이동할 곳에 x * 2 값을 저장
                    x = 0 # 블록을 더했으므로 x 초기화
                    p -= 1 # 행에서 갈 수 있는 가장 하단을 채웠으므로 다음 블록이 이동하게될 위치 감소
                else: # 지난 블록과 같지 않은 경우
                    board[p][i] = x # 이동할 곳에 지난 블록인 x값을 저장
                    x = board[j][i] # 이전 블록을 새로운 블록으로 변경
                    p -= 1 # 행에서 갈 수 있는 가장 하단을 채웠으므로 다음 블록이 이동하게될 위치 감소
            board[j][i] = 0 # 블록 이동했으므로 비워줌
        if x != 0: board[p][i] = x  # 행의 가장 상단까지 도달 후에 이동할 블록이 남아있으면 블록 이동
    return board

def move_right(board):
    for i in range(N): # 행
        p = N - 1 # 열의 가장 우측
        x = 0
        for j in range(N - 1, -1, -1): # 열
            if board[i][j] == 0: continue # 비어있으면 continue
            if x == 0: x = board[i][j] # x가 비어있으면 더해줄 이전 블록이 없다는 것이므로 x를 변경
            else:
                if x == board[i][j]: # 지난 블록과 같은 경우
                    board[i][p] = x * 2 # 이동할 곳에 x * 2 값을 저장
                    x = 0 # 블록을 더했으므로 x 초기화
                    p -= 1 # 열에서 갈 수 있는 가장 우측을 채웠으므로 다음 블록이 이동하게될 위치 감소
                else:  # 지난 블록과 같지 않은 경우
                    board[i][p] = x # 이동할 곳에 지난 블록인 x값을 저장
                    x = board[i][j] # 이전 블록을 새로운 블록으로 변경
                    p -= 1 # 열에서 갈 수 있는 가장 우측을 채웠으므로 다음 블록이 이동하게될 위치 감소
            board[i][j] = 0 # 블록 이동했으므로 비워줌
        if x != 0: board[i][p] = x # 열의 좌측 끝까지 도달 후에 이동할 블록이 남아있다면 블록 이동
    return board

def move_left(board):
    for i in range(N): # 행
        p = 0 # 열의 가장 좌측
        x = 0
        for j in range(N): # 열
            if board[i][j] == 0: continue # 비어있으면 continue
            if x == 0: x = board[i][j] # x가 비어있으면 더해줄 이전 블록이 없다는 것이므로 x를 변경
            else:
                if x == board[i][j]: # 지난 블록과 같은 경우
                    board[i][p] = x * 2 # 이동할 곳에 x * 2 값을 저장
                    x = 0 # 블록을 더했으므로 x 초기화
                    p += 1 # 열에서 갈 수 있는 가장 좌측을 채웠으므로 다음 블록이 이동하게될 위치 증가
                else:
                    board[i][p] = x # 이동할 곳에 지난 블록인 x값을 저장
                    x = board[i][j] # 이전 블록을 새로운 블록으로 변경
                    p += 1 # 열에서 갈 수 있는 가장 좌측을 채웠으므로 다음 블록이 이동하게될 위치 증가
            board[i][j] = 0 # 블록 이동했으므로 비워줌
        if x != 0: board[i][p] = x # 열의 우측 끝까지 도달 후에 이동할 블록이 남아있다면 블록 이동
    return board


def backTracking(board_,cnt)  :
    global result
    if cnt == 5 :
        for i in range(N) :
            for j in range(N) :
                result = max(result,board_[i][j])
        return

    backTracking(move_up(deepcopy(board_)),cnt+1)
    backTracking(move_down(deepcopy(board_)),cnt+1)
    backTracking(move_right(deepcopy(board_)),cnt+1)
    backTracking(move_left(deepcopy(board_)),cnt+1)

backTracking(board,0)
print(result)
