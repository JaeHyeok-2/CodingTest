# https://programmers.co.kr/learn/courses/30/lessons/17676

def solution(lines):
    answer = 0
    start_time = []
    end_time = []
    for line in lines:
        time = line.split(' ')
        start_time.append(startTime(time[1], time[2]))
        end_time.append(getTime(time[1]))

    for i in range(len(lines)):
        cnt = 0
        cur_end_time = end_time[i]
        for j in range(i, len(lines)):
            if cur_end_time > start_time[j] - 1000:
                cnt += 1
        answer = max(cnt, answer)
    return answer


def getTime(time):
    h = int(time[:2]) * 3600
    m = int(time[3:5]) * 60
    s = int(time[6:8])
    ms = int(time[9:])
    return (h + m + s) * 1000 + ms


def startTime(time, processTime):
    pT = int(float(processTime[:-1]) * 1000)
    return getTime(time) - pT + 1

