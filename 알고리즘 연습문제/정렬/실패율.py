# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3
def solution(N,stages) :
    answer = []
    length = len(stages)
    for i in range(1,N+1):
        count = stages.count(i)
        if length == 0 :
            fail = 0
        else :
            fail = count/length
        answer.append((i,fail))
        length -=count

    #정렬
    answer =sorted(answer,key = lambda x :x[1],reverse = True) # answer[1]의 값으로 내림차순으로 정렬
    answer= [i[0] for i in answer] # answer의 첫번째 원소만 뽑기
    return answer