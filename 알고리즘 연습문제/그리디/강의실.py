#https://www.acmicpc.net/problem/1374

"""
N개의 강의가 있다. 우리는 모든 강의의 시작하는 시간과 끝나는 시간을 알고 있다. 이때, 우리는 최대한 적은 수의 강의실을 사용하여 모든 강의가 이루어지게 하고 싶다.
물론, 한 강의실에서는 동시에 2개 이상의 강의를 진행할 수 없고, 한 강의의 종료시간과 다른 강의의 시작시간이 겹치는 것은 상관없다. 필요한 최소 강의실의 수를 출력하는 프로그램을 작성하시오.
"""
import sys
import heapq
input =sys.stdin.readline

n= int(input())
heap = [] # 시작,끝,번호 담을 힙
q=  [] # 끝나는시간을 담을 힙  q의 길이가 곧 강의실의 개수이다.

for _ in range(n) :
    id,start,end = map(int,input().split())
    heapq.heappush(heap,(start,end,id))

# 첫번째강의실 생성
start,end,id = heapq.heappop(heap)
heapq.heappush(q,end) # 끝나는 시간을 차례대로 입력할 것인데, 시작시간은 오름차순

while heap : #모든 강의를 탐색
    start,end,id = heapq.heappop(heap)
    print(start)
    if q[0] <=start :  #만약 전에 있던 강의끝나는시간 보다! 더 늦게 시작한다면 이강의실은 같이쓸 수 있다
        heapq.heappop(q) #강의실 같이쓰기
    heapq.heappush(q,end) # 만약 if문을 통과했다면, end시간을 뒤의 강의시간으로 바꿈
                          # 그게아니라면 강의실을 하나 추가한거 일뿐
print(len(q))