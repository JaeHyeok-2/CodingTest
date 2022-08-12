# https://programmers.co.kr/learn/courses/30/lessons/60059 자물쇠와 열쇠

def rotate_90(key):
    length = len(key)
    temp = [[0]*length for _ in range(length)] # 90도 회전후 반환 할 배열
    for i in range(length):
        for j in range(length) :
            temp[j][length-i-1] = key[i][j]
    return temp

#lock이 열렸는가?
def check(new_lock):
    length = len(new_lock)//3
    for i in range(length,length*2):
        for j in range(length,length*2):
            if new_lock[i][j] != 1: # 홈이 안맞는 부분이 존재한다면?
                return False    #실패
    return True     #홈이 다맞을경우 True

def solution(key,lock) :
    m,n = len(key),len(lock)
    new_lock = [[0]*(n*3) for _ in range(n*3)]

    #3배 넓게만든 lock 가운데 값 채우기 (1,1)
    for i in range(n):
        for j in range(n) :
            new_lock[i+n][j+n] = lock[i][j]

    for rotation in range(4) :
        key= rotate_90(key)
        for x in range(n*2):
            for y in range(n*2):

                for i in range(m):
                    for j in range(m):
                        new_lock[i+x][j+y] +=key[i][j]
                #홈 확인결과
                if check(new_lock):
                    return True

                #아닐경우 원위치
                for i in range(m):
                    for j in range(n):
                        new_lock[i+x][j+y] -=key[i][j]
    return False #모두 해봐도 안될경우


key = [[0,0,1],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]

print(solution(key,lock))