# https://programmers.co.kr/learn/courses/30/lessons/42891
import heapq


def solution(food_times, k):
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    previous = 0
    sum_previousTime = 0
    length = len(food_times)

    while sum_previousTime + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_previousTime += (now - previous) * length
        previous = now
        length -= 1

    result = sorted(q, key=lambda x: x[1])
    if not result:
        return -1
    return result[(k - sum_previousTime) % length][1]