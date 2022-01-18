# 프로그래머스 https://programmers.co.kr/learn/courses/30/lessons/60062
from itertools import permutations
def solution(n, weak, dist):
    length = len(weak) #점검할 외벽의 개수
    answer = len(dist) + 1  # 최대 인원수 +1

    for i in range(length):
        weak.append(weak[i] + n)
        """
        원형의 식탁을 하나의 열로 나열 한 식
        1 3,5,10의 시계모양 --> 1,3,5,10,13,15,17,22 
        """

    for start in range(length): # 위의 일렬로 나열된 배열에서 점검 개수씩 끊어서 탐색
        for friends in list(permutations(dist, len(dist))): # 모든 점검할 수 있는 순서를 나열
            count = 1
            position = weak[start] + friends[count - 1] # 각 친구가 점거하는 거리의 구간

            for index in range(start, start + length):
                if position < weak[index]: # 점검 범위를 다 돌지못하면,
                    count += 1 # 친구를 한명더 추가
                    if count > len(dist): #친구를 모두 불러도 안될경우
                        break #종료
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

print(solution(n,weak,dist))