# https://www.acmicpc.net/problem/16953

"""
A -> B 문제로,
정수 A 를 정수 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 2가지
    # 2를 곱한다
    # 1을 수의 가장 오른쪽에 추가한다.

"""
from collections import deque
a,b = map(int,input().split())

q = deque()
q.append((b,1))
flag = False
ans = 1
while q :
    now,cnt = q.popleft()
    if now <a : break

    if now == a :
        flag = True
        ans = cnt
        break
    if now%10 == 1 :
        q.append((now//10,cnt+1))

    if now%2 == 0 :
        q.append((now/2,cnt+1))

if flag :
    print(ans)
else :
    print(-1)