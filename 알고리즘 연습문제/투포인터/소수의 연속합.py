import sys
input = sys.stdin.readline
n= int(input())

# 에라토스 테네스체 + 투포인터 같은데
def isPrime(n) :
    lst = [False]*(n+1)
    m = int(n**0.5)

    for i in range(2,m+1) :
        if not lst[i] :
            for j in range(2*i,n+1,i) :
                lst[j] = True
    return [i for i in range(2,n+1) if lst[i] == False]

prime = isPrime(n)

length = len(prime)
start = 0
end = 0
interval_sum = 0
count = 0

for start in range(length) :
    while interval_sum < n and end < length :
        interval_sum += prime[end]
        end +=1

    if interval_sum == n :
        count +=1
    interval_sum -= prime[start]

print(count)