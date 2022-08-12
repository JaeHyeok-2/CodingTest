from collections import defaultdict #
from sys import stdin
input =stdin.readline

T = int(input()) # TestCase 개수
n = int(input()) # 첫번째 배열 원소의 개수
A = list(map(int,input().split()))
m = int(input().split()) # 두번째 배열 원소의 개수
B = list(map(int,input().split()))

PrefixSum_A = defaultdict(int)
PrefixSum_B = defaultdict(int)

for i in range(n) :
    for j in range(i,n) :
        PrefixSum_A[sum(PrefixSum_A[i:j+1])] +=1

for i in range(m) :
    for j in range(i,m) :
        PrefixSum_B[sum(PrefixSum_B[i:j+1])] +=1

answer = 0

for key in PrefixSum_A.keys() :
    answer += PrefixSum_A[key] * PrefixSum_B[T-key]
print(answer)