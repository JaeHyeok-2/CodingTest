n = (input())
zero = 0
one = 0
start = n[0]
if start =='0' :
    zero +=1
else :
    one +=1

for i in range(1,len(n)) :
    if n[i-1] == n[i] :
        continue
    elif n[i] == '1':
        one+=1
    else :
        zero+=1
print(min(zero,one))
