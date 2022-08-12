# https://www.acmicpc.net/problem/1987
import sys
#sys.setrecursionlimit(10**4)
input= sys.stdin.readline
n,m = map(int,input().split())
board = [list(input().strip()) for _ in range(n)]

alphabet = set()
alphabet.add(board[0][0])

dr = [1,0,-1,0]
dc = [0,1,0,-1]

res = 0
def backTracking(r,c,count) :
    global res
    res = max(res,count)

    for i in range(4) :
        nr = r + dr[i]
        nc = c + dc[i]
        # 보드크기 내에 존재하며, 알파벳이 이미 나오지않았을경우,
        if 0<=nr<n and 0<=nc<m and (board[nr][nc] not in alphabet):
                alphabet.add(board[nr][nc])
                backTracking(nr,nc,count+1)
                # 끝날경우, 알파벳을 뺀다
                alphabet.remove(board[nr][nc])
backTracking(0,0,1)
print(res)
