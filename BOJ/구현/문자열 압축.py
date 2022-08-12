#   https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(text) :
    answer = len(text)
    for step in range(1,len(text)//2+1) :
        compressed = ""
        prev = text[0:step]
        count = 1
        for j in range(step,len(text),step):
            if prev == text[j:j+step]:
                count +=1
            else :
                compressed += str(count) + prev if count>=2 else prev
                count,prev =1,text[j:j+step]
                answer = min(answer,len(compressed))
        compressed += str(count) + prev if count>=2 else prev
        answer = min(answer,len(compressed))
    return answer

