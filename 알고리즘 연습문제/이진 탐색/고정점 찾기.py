# 고정점 : 원소의 값이 인덱스와 동일한 원소
# 문제에서는 각 배열당 최대 1개까지 고정점이 존재할 수 있음
# 고정점이 존재한다면, 그 인덱스를 출력, 없다면 -1 출력
def binarySearch(array,left,right) :
    if left > right :
        return None
    mid = (left+ right)//2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binarySearch(array,left,mid-1)
    else :
        return binarySearch(array,mid+1,right)

n = int(input())
array = list(map(int,input().split()))

index = binarySearch(array,0,n-1)
if index ==None :
    print('-1')
else :
    print(index)
