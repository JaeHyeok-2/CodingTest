# https://www.acmicpc.net/problem/15686
# 순열,브루트포스,구현 문제
from itertools import combinations  #조합을 사용하기 위해 itertools 사용
n,m = map(int,input().split())
chicken,house =[],[]    #치킨, 집을 구별하여 배열로 생성

for r in range(n):
    data = list(map(int,input().split()))
    for c in range(n):
        if data[c] == 1 :
            house.append((r,c))
        elif data[c] == 2 :
            chicken.append((r,c))
candidates = list(combinations(chicken,m))   #치킨집중 m개를 선택

def get_sum(candidate):
    result = 0
    for hx,hy in house :
        temp = 1e9
        for cx,cy in candidate :
            temp = min(temp,abs(hx-cx) + abs(hy-cy))
        result +=temp
    return result

result = 1e9
for candidate in candidates:
    result =min(result,get_sum(candidate))

print(result)


