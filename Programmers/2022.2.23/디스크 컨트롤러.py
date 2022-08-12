# https://programmers.co.kr/learn/courses/30/lessons/42627
import heapq

def solution(jobs) :
    answer,now,index = [0] *3
    start = -1
    q = []

    # jobs 리스트의 값을 모두 사용할때까지
    while index < len(jobs) :
        for i in jobs :
            # jobs의 요청시간에 대해서, 이전 작업시간의 끝보다는 크고, 현재 시점보다는 작거나 같을경우
            if start < i[0] <= now :
                heapq.heappush(q,(i[1],i[0])) # 작업시간이 짧은거를 순서대로 실행

        #만약 실행할 작업이 있다면,
        if len(q) > 0 :
            current = heapq.heappop(q)
            # 이전 작업 시간 start값을 now값으로 대체하고,
            start =now
            # now값은 현재시점 + 들어온 작업이 끝나는 시점으로 갱신
            now += current[0]
            #answer: 현재시점 now에서 작업이 들어온 요청시간을 빼준다
            answer += (now - current[1])
            # 작업이 하나끝났으므로 , index는 1증가 시켜준다
            index +=1

        # 이 범위내에 실행할 작업이 없다면
        else :
            now +=1 # 현재 시점을 1초뒤로 미뤄준다. (또없으면 계속 1초씩증가시키겠지?)

    return int(answer/len(jobs))