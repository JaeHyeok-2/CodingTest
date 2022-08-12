from sys import stdin
input = stdin.readline

def first(array,target,left,right) :
    if left > right :
        return None
    mid = (left + right) // 2
    if array[mid] == target and (mid == 0 or array[mid-1] < array[mid]) :
        return mid
    elif array[mid] >=target :
        return first(array,target,left,mid-1)
    else :
        return first(array,target,mid+1,right)

def last(array,target,left,right) :
    if left > right :
        return None
    mid = (left + right)//2
    if array[mid] == target and (mid == n-1 or array[mid+1]> array[mid]) :
        return mid
    elif array[mid] > target :
        return last(array,target,left,mid-1)
    else :
        return last(array,target,mid+1,right)

def count_by_range(array,x) :
    a = first(array,x,0,n-1)
    b = last(array,x,0,n-1)
    if a == None :
        return 0
    return b-a+1

n = int(input())
array = list(map(int,input().split()))
array.sort()
m = int(input())
card = list(map(int,input().split()))

for i in card :
    print(count_by_range(array,i),end = " ")
