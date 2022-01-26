def slidingWindow(array,k) :
    max_sum = float('-inf')
    start = 0 # 시작점
    interval_sum = 0 # 구간합 초기화

    for end,val in enumerate(array) :
        interval_sum +=val
        #고정된 배열의 개수를 k 라고 하면, k = end - start + 1로 표현 가능
        if k == end -start + 1 :
            max_sum = max(max_sum,interval_sum)

            interval_sum -=array[start]
            start+=1

    return max_sum

array = [3,2,1,5,6,7]
k = 3
print(slidingWindow(array,k))
