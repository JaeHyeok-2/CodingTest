from sys import stdin
input = stdin.readline

def mulMatrix(n,matrix1,matrix2) :
    result = [[0] * n for _ in range(n)]
    for i in range(n) :
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %=1000
    return result

def divide_and_quenqer(n,m,matrix):
    if m == 1 :
        return matrix
    elif m== 2 :
        return mulMatrix(n,matrix,matrix)
    else :
        tmp = divide_and_quenqer(n,m//2,matrix)
        if m%2 == 0 :
            return mulMatrix(n,tmp,tmp)
        else :
            return mulMatrix(n,mulMatrix(n,tmp,tmp),matrix)


n,m = map(int,input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))

result = divide_and_quenqer(n,m,matrix)

for i in range(n):
    for j in range(n):
        print(result[i][j]%1000,end = ' ')
    print()