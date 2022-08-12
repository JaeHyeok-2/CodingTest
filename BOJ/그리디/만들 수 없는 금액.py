n = int(input()) # 만들어야 하는 금액
coin = list(map(int,input().split())) # 동전
# 1 1 2 3 9 로만들수 있는 돈
# 1,2,4,7, 이전것들의 합이 다음거보다 작다면, 그 동전은 만들수 없음
coin.sort()
result = coin[0]
for i in range(1,len(coin)) :
    if result < coin[i]:
        result +=1
        break
    else :
        result+=coin[i]
print(result)
