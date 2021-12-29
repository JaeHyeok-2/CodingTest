#순열을 이용한 풀이
import sys
from itertools import permutations
input =sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
op_num = list(map(int,input().split()))
op_kind = ['+','-','*','/']
op = []
for i in range(len(op_num)) :
    for j in range(op_num[i]):
        op.append(op_kind[j])
maximum = -1e9
minimum = 1e9

def solve():
    global maximum,minimum
    for case in permutations(op,(n-1)):
        total = data[0]
        for r in range(1,n):
            if case[r-1] == '+' :
                total +=data[r]
            elif case[r-1] == '-':
                total -=data[r]
            elif case[r-1] == '*':
                total *=data[r]
            elif case[r-1] == '/':
                total = int(total/data[r])

        maximum = max(maximum,total)
        minimum = min(minimum,total)
solve()
print(maximum)
print(minimum)
