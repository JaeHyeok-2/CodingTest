"""
탑승시간순으로 정렬 후 

"""
from collections import deque  # deque


def transform(timetable):
    renewal = []
    for time in timetable:
        t = time.split(":")  # 시간, 분으로 쪼갠후
        hTom = int(t[0]) * 60
        m = int(t[1])
        renewal.append(hTom + m)
    renewal.sort(reverse=True)
    return renewal


def HHMM(time):
    temp = ''
    # HH:
    if time // 60 < 10:
        temp = '0' + str(time // 60)
    else:
        temp = str(time // 60)

    time -= 60 * (time // 60)
    temp += ":"

    if time // 10 == 0:
        temp += '0' + str(time)
    else:
        temp += str(time)

    return temp


def solution(n, t, m, timetables):
    answer = ''

    timetable = transform(timetables)
    # print(timetable)

    bus_idx = 0
    # 버스 시간표 만들기 
    busTable = [540 + (i * t) for i in range(n)]  # t : 배차간격 , i  버스 개수

    tmp_time = 0

    while bus_idx < len(busTable):
        # 2가지 테스트 케이스 
        bus = []
        cnt = 0  # 탑승자 count

        while cnt != m:
            # 탑승이 가능 조건 : 버스배차시간 전에오거나, 탈사람이 있어야함
            if len(timetable) >= 1 and busTable[bus_idx] >= timetable[len(timetable) - 1]:
                bus.append(timetable.pop())
                cnt += 1
                # 탈사람이 없을 경우,
            else:
                break
                # 마지막 버스인데,
        if bus_idx == len(busTable) - 1:
            # 정원이 다차있다면, 
            if cnt == m:
                tmp_time = bus.pop() - 1
            else:
                # 정원이 모두 차있지 않았을경우 ,
                tmp_time = busTable[bus_idx]

        bus_idx += 1

    answer = HHMM(tmp_time)

    return answer