# https://programmers.co.kr/learn/courses/30/lessons/60062/solution_groups?language=python3
"""
    # 문제에서 중요한점은 "최소한의 인원수를 구하시오"
    # 가장 범위가 넓게 점검할 수 있는 인력을 우선으로 점검을 실시 : dist를 내림차순으로 설정
    # queue를 이용해서 각 인원에 대한 범위를 좁혀나가서, queue 내부에는 점검하지 못한 범위를 삽입
      ex) 첫번째 인력이 범위가 4를 탐색한다면, [1,5,6,10]에서 [6,10], [1,10], [1,5]를 탐색하지 못하므로 3개를 큐에 삽입
          다음 인력은 [6,10],[1,10],[1,5]를 탐색 실시
    # 중복이 발생하지 않도록 visited는 set() 으로 설정

"""
from collections import deque

def solution(n,weak,dist) :
    dist.sort(reverse =True)
    q = deque([weak])
    visited = set()
    visited.add(tuple(weak))

    for i in range(len(dist)):  # 모든 인력에 대해서 탐색 실시
        d = dist[i]
        for _ in range(len(q)) :    #queue에는 점검을 하지않은 값들의 배열이 저장
            current = q.popleft()   #초기 current = [1,5,6,10]
            for p in current :      #[1,5],[5,9],[6,10],[10,14==2] 를 탐색 한후 이 범위 밖에있는 튜플들은 다시 visited 에 삽입
                l = p # 왼쪽
                r = (p+d)%n
                if l < r :
                    temp = tuple(filter(lambda x: x<l or x > r, current))   #filter를 통해, 범위밖의있는 값들을 temp에 tuple형태로 저장
                else:
                    temp = tuple(filter(lambda x: x<l and x>r,current))

                if len(temp) == 0 : # temp 가 없다는것은 더이상 점검할 외벽이 없다는 뜻
                    return i+1  #그때의 i+1은 투입한 인원의 수
                elif temp not in visited:
                    visited.add(temp)
                    q.append(list(temp))

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

print(solution(n,weak,dist))