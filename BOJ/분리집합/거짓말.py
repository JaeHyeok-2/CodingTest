#   https://www.acmicpc.net/problem/1043

"""
메서드 알아두기 set()
add() : 집합에 원소 추가
update() : 집합에 원소 여러개 추가
set.union(a,b) : a와 b의 합집합 ---> a|b
set.intersection(a,b) : a,b의 교집합 ---> a & b
set.difference(a,b) : a,b의 차집합 ---> a-b

"""
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
witness_set = set(input().rstrip().split()[1:]) # 사실을 아는 사람들

parties = [] # 각 파티마다 참석하는 사람들의 번호
res = [] # 각파티에서 진실을 말할수 있는가 1 없으면 0

for _ in range(m):
    parties.append(set(input().rstrip().split()[1:])) # 처음 파티의 인원수는 필요 없으므로 입력에서 뺀다
    res.append(1) # 모든 파티에 참석가능으로 초기화

for _ in range(m) :
    for i,party in enumerate(parties) : # enumerate 로 i는 현재 어느 파티인가, party는 그 파티에 참석하는 사람들
        if witness_set & party :
            res[i] = 0 # 사실을 아는 사람이있으면, 과장을 못하므로 0
print(sum(res))





