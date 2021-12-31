def count_by_value(array,x) :
    n = len(array)
    a = first(array,x,0,n-1)
    b = last(array,x,0,n-1)
    if a ==None :
        return 0
    return b-a+1

def first(array,target,left,right) :
    if left >right :
        return None
    mid = (left+right)//2
    if array[mid] == target and (array[mid-1] <target or mid == 0) :
        return mid
    elif array[mid]>= target:
        return first(array,target,left,mid-1)
    else :
        return first(array,target,mid+1,right)

def last(array,target,left,right) :
    if left> right :
        return None
    mid = (left+right)//2
    if array[mid] == target and (array[mid+1] > target or mid == n-1) :
        return mid
    elif array[mid] >target :
        return last(array,target,left,mid-1)
    else :
        return last(array,target,mid+1,right)
n,x = map(int,input().split())
array = list(map(int,input().split()))

count = count_by_value(array,x)
if count == 0 :
    print(-1)
else :
    print(count)