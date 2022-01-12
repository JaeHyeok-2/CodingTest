"""
한 마을에 모험가 N 명 존재, N명을 대상으로 공포도 측정
공포도가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어진다
따라서 공포도가 X인 모험가는 반드시 X명이상으로 구성한 모험가 그룹에 참여해야할때,
최대로 만들 수 있는 그룹수는?
"""
n = int(input())
guild = list(map(int,input().split()))

guild.sort() #오름차순설정
count = 0
result = 0
for i in guild :
    count+=1
    if count>=i :
        result+=1
        count = 0
print(result)