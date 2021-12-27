# O(M^3)으로 완전탐색 구현
def possible(answer) :
    for x,y,stuff in answer :
        if stuff == 0 : #기둥일경우 : 밑,바닥,보의 맨끝에 걸쳐있을때
            if [x,y-1,0] in answer or y ==0 or [x,y,1] in answer or [x-1,y,1] in answer :
                continue
            else :
                return False
        elif stuff == 1 : # 보의 경우 : 기둥위,보사이
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer) :
                continue
            else :
                return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame :
        x,y,stuff,operate = frame
        if operate == 1 : #설치
            answer.append([x,y,stuff])  #배열을 넣은후,
            if not possible(answer) :   #건축이 불가능하다면, 삭제
                answer.remove([x,y,stuff])
        else : #삭제
            answer.remove([x,y,stuff])
            if not possible(answer) :
                answer.append([x,y,stuff])
    return sorted(answer,key =lambda x : (x[0], x[1],x[2]))