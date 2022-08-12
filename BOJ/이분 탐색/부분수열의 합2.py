# https://www.acmicpc.net/problem/1208

import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

# 가운데를 기점으로 두개의 배열로 나눈다.
arr1 = a[:n // 2]
arr2 = a[n // 2:]

# 나눈후, 각 왼쪽, 오른쪽의 값들 조합으로 새로운 배열 생성
left, right = [], []
for i in range(len(arr1) + 1):
    data = combinations(arr1, i)
    for l in data:
        left.append(sum(l))

for i in range(len(arr2) + 1):
    data = combinations(arr2, i)
    for l in data:
        right.append(sum(l))
# left에는 오름차순 , right 는 내림차순 (pointer 이동에 편리함)
left.sort()
right.sort(reverse=True)

# print(left,right,sep = '\n')

# lp : left의 위치 포인터 , rp : right의 위치 포인터
lp, rp = 0, 0
answer = 0
while lp < len(left) and rp < len(right):
    tmp = left[lp] + right[rp]  # 현재값

    # 현재값이 s라면, 같은값이 존재하는지 구해본다.
    if tmp == s:
        lp += 1
        rp += 1

        c1 = 1
        c2 = 1
        # left에 다음칸 값과 같다면,
        while lp < len(left) and left[lp] == left[lp - 1]:
            c1 += 1
            lp += 1
        # 오른쪽 다음칸 값과 같다면,
        while rp < len(right) and right[rp] == right[rp - 1]:
            c2 += 1
            rp += 1
        # c1,c2의 곱은 순서쌍 곱이다.
        """
         1, 1, 1, 2,3
        -1,-1,-1, 5,10  에서  c1 = 3 ,c2 = 3이므로 순서쌍은 총 9개

        """
        answer += (c1 * c2)

    elif tmp < s:
        lp += 1
    else:
        rp += 1
# s가 0이라면 , 공집합 데이터를 빼주어야하므로 -1
if s == 0:
    answer -= 1
print(answer)

