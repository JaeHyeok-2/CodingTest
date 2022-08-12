# https://www.acmicpc.net/problem/5397
import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    pwd = list(input().replace("\n",""))
    left,right = [],[]
    for value in pwd :
        # 왼쪽 커서 일경우,
        if value == "<" :
            if len(left) != 0 :
                right.append(left.pop())
        elif value == ">" :
            if len(right) != 0 :
                left.append(right.pop())
        elif value == "-" :
            if len(left) != 0 :
                left.pop()
        else :
            left.append(value)

    left_string = "".join(left)
    right_string = "".join(right[::-1])
    print(left_string + right_string)
