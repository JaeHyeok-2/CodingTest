n,m,k = map(int,input().split())

def divide(n,m) :
    global k
    if m == 1 :
        return n%k
    temp = divide(n,m//2)
    if m %2 == 0 :
        return temp *temp %k
    else :
        return (temp*temp%k) * n %k
print(divide(n,m))