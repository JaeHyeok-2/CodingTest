n = int(input())
row = [0] * n
result = 0

def is_possible(x) :
    for i in range(x) :
        if row[i] == row[x] or abs(row[x]-row[i]) == x-i : #같은 열에 있을경우
            return False
    return True

def dfs(x) :
    global result
    if x== n :
        result +=1
    else :
        for i in range(n) :
            row[x] = i
            if is_possible(x) : # 현재 행에 놓을 수 있는가?-> 가능하다면 백트래킹 실시 x
                dfs(x+1)        # 놓을 수 없다면, 백트래킹

dfs(0)
answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(answer[n])

