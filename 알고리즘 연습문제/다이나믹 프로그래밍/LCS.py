string_A = str(input())
string_B = str(input())

LCS = [[0] *(len(string_A)+1) for _ in range(len(string_B)+1)] # column = A  , row = B


for i in range(1,len(string_B)+1):
    for j in range(1,len(string_A)+1) :
        if string_B[i-1] == string_A[j-1] :
            LCS[i][j] = LCS[i-1][j-1] +1
        else :
            LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])
print(LCS[len(string_B)][len(string_A)])