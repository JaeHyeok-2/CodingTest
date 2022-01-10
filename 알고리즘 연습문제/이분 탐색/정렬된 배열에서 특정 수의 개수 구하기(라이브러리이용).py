from bisect import bisect_left,bisect_right

def count_by_range(a,left_value,right_value):
  right_index = bisect_right(a,right_value) #해당 값중 제일 오른쪽에 있는값
  left_index=  bisect_left(a,left_value)    # 해당 값중 제일 왼쪽에 있는값
  return right_index - left_index

n,x = map(int,input().split())
array = list(map(int,input().split()))

count = count_by_range(array,x,x)
if count == 0 :
    print(-1)
else :
    print(count)