n =input()
answer =0
for i in range(len(n)):
    if n[i] =='0' or n[i] == '1' :
        answer +=int(n[i])
    else :
        if answer == 0 :
            answer = int(n[i])
            continue
        answer *=int(n[i])
print(answer)