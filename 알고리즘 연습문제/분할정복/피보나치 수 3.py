"""
피사노 주기

주기의 길이가 P이면 , N 번째 피보나치 수를 M 으로 나눈 나머지는 N%P번째 피보나치 수를 M으로 나눈 나머지와 같다.
M = 10^k 일때  k>2라면, 주기는 항상 15 x 10^k-1 이다.
"""
n = int(input())
MOD = int(1e6)
p = int(MOD/10) * 15
fib = [0] *(p+1)
fib[1] =1

for i in range(2,p) :
    fib[i] = fib[i-1] +fib[i-2]
    fib[i] %=MOD

print(fib[n%p])

