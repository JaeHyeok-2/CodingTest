n,m = map(int,input().split()) # 볼링공 개수 =n , 공의 최대 무게 = m
weight = [0] *11  #볼링공 무게는 1~10  index = 무게, 배열값 = 공의 개수
number = list(map(int,input().split()))

for i in number :
    weight[i] +=1
result = 0
for i in range(1,m+1) :
    n-=weight[i]
    result += (n * weight[i])
print(result)