# https://programmers.co.kr/learn/courses/30/lessons/43238
"""
접근을 어떻게 했어야 하는 지 몰랐던 문제
left = 1 , right = 최대 걸리는 시간 max(times) *n
mid = (left+right)//2 로
mid 시간내에 입국 심사를 모두가능하다면? right = mid-1로 시간을 줄인다
mid 시간내에 입국 심사를 불가능하다면? left = mid-1 시간을 늘려본다
"""

def solution(n,times) :
    left,right =1, max(times) *n
    while left<=right:
        mid = (left+right)//2
        total = 0  # 입국심사 가능인원
        for time in times :
            total += mid//time
            """
            n = 6 , times  = [7,10] 일때, 1) mid = 30 일때 total = 4+3 = 7 로 30초일때는 입국심사가 가능
            따라서 ,right = mid-1로 축소
            """
        if total >=n :
            right = mid-1
        else :
            left = mid+1
    return left

n,times = 6,[7,10]
print(solution(n,times))
