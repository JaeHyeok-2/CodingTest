# https://www.acmicpc.net/problem/2110
"""
    만약 1,2,3,4,6,7,8,9,11,12 가 있다고 가정해보자.
    2개를 설치한다면, 1,12를 설치해서 max =11로 구할수 있지만,
    3개를 설치한다면?
    # 거리의 최대값을 구하는것이기 때문에, distance_min = (1,2) distance_max = (1,12)가 있다
    3개라면 이 중점에 설치하는것이 가장 이상적이다.
    즉 거리차가 [1,11]에 사이값, 즉 6에 설치한다면 최대거리는 (6,12), 최소거리는 (1,6) 을통해 5가 될수 있음을 알수있다
    mid = (1+11)//2  = 6

    3개 설치시 진행상태
    mid = 6이므로,
    1. 거리가 6씩 떨어진곳에 안테나를 설치해본다
    # 1,7,13 --> 13이 존재하지않는다. 현재 2개설치
    # 3개를 설치해야하므로 간격을 좁혀야한다 "이때" 좁히는 방식은 이분탐색으로 right = mid-1을뺀다면?
    left = 1 ,right = 5 이므로 mid = 3 즉 3칸의 간격씩 공유기를 설치해본다

    2. 거리가 3씩 떨어진 칸에 안테나 설치
    # 1,4,7,11 --> 4개 존재 // 일단 최대거리 3 임을 저장
    # 하지만 3개설치로 조금더 줄일수 있지않을까?
    # 이때, 간격을 조금더 넓히기위해, left = mid+1로 조절
    # left = mid+1 --> left = 4
    # right = 5
    mid = 4임을 알 수 있다

    3.거리가 4씩 떨어진 칸에 안테나 설치
    # 1,5,9 --> 성립한다. 이전의 최대값인 3에서 4로 갱신 후 , 더 넓힐수 있는지 확인
    # left = mid + 1 =  5 , right = 5 이므로 left<=right가 성립

    4.거리가 5씩 떨어진 칸에 안테나를 설치
    # 1,6,11 이 3개로 성립한다. 따라서 ,최대값을 5로 갱신후 더 넓힐 수 있는 지확인
    # left = mid+1로 확장 -->left =6, right = 5
    # left<=right가 아니므로 종료
    따라서 결과값 5가 최대값

"""
n,c = map(int,input().split())
array = []
for _ in range(n) :
    array.append(int(input()))
array.sort()
def binarySearch(array,left,right) :
    while left<=right :
        mid = (left+right)//2
        count = 1
        current = array[0]

        for i in range(1,n) :
            if array[i] >=current + mid :
                count+=1
                current =array[i]
        if count >=c :
            global answer
            answer = mid
            left = mid+1
        else :
            right = mid-1
left = 1
right = array[-1]- array[0]
answer = 0
binarySearch(array,left,right)
print(answer)