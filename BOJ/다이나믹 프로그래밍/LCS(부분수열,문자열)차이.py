# Longest Common Subsequence  가장긴 공통 문자열
string_A = str(input())
string_B = str(input())

len_A,len_B = len(string_A), len(string_B)
LCS = [[0] *(len(string_A)+1) for _ in range(len(string_B)+1)] # column = A  , row = B

"수열일때"
for i in range(len_A+1) :
    for j in range(len_B+1) :
        if i == 0 or j ==0 :
            LCS[i][j] = 0
        elif string_A[i] == string_B[j]:
            LCS[i][j] = LCS[i-1][j-1] +1
        else :
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])


"문자열일때"
for i in range(len_A+1):
    for j in range(len_B+1):
        if i == 0 or j == 0 :
            LCS[i][j] =0
        elif string_A[i] == string_B[j]:
            LCS[i][j] = LCS[i-1][j-1] +1
        else :
            LCS[i][j] =0


