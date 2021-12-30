import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
board = []
teacher = []
blank = []
for i in range(n) :
  data = list(input().split())
  board.append(data)
  for j in range(n):
    if board[i][j] == 'X':
      blank.append((i,j))
    if board[i][j] == 'T':
      teacher.append((i,j))
# 동 서 남 북
# 학생을 발견시 True , 장애물 발견시 False 반환
def search(r,c,dir) :
  if dir == 0 :
    while c < n :
      if board[r][c] == 'S':
        return True
      elif board[r][c] =='O' :
        return False
      c+=1
  if dir == 1 :
    while c >=0 :
      if board[r][c] =='S' :
        return True
      elif board[r][c] == 'O':
        return False
      c -=1
  if dir == 2 :
    while r < n :
      if board[r][c] == 'S' :
        return True
      elif board[r][c] =='O':
        return False
      r +=1

  if dir == 3 :
    while r >=0 :
      if board[r][c] == 'S' :
        return True
      elif board[r][c] =='O' :
        return False
      r-=1


result = False
def check() :
  for x,y in teacher :
    for i in range(4) :
      if search(x,y,i) :
        return True
  return False

for case in combinations(blank,3):
  for x,y in case :
    board[x][y] ='O'
  if not check() :
    result = True
    break
  for x,y in case :
    board[x][y] = 'X'


if result :
  print("YES")
else :
  print("NO")

