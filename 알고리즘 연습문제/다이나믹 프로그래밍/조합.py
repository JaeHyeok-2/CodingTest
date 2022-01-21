# https://www.acmicpc.net/problem/2407
# nCm = n

n,m = map(int,input().split())

fib_M = [1]*(n+1)
#분모의 팩토리얼 수
for i in range(2,n+1):
    fib_M[i] = fib_M[i-1] *i

fib_N = [1]*(m+1)
fib_N[1] = n
#분자의 팩토리얼

for i in range(2,m+1) :
    fib_N[i] = fib_N[i-1] *(n-1)
    n-=1

print(fib_N[m]//fib_M[m])