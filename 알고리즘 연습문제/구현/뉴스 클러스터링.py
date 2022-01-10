# 프로그래머스
#https://programmers.co.kr/learn/courses/30/lessons/17677

from collections import Counter

def solution(str1, str2):
    answer = 0
    str1 = str1.lower() #소문자로 변경후,
    str2 = str2.lower()

    str1_list = []
    str2_list = []

    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            str1_list.append(str1[i:i + 2])
    for j in range(len(str2) - 1):
        if str2[j].isalpha() and str2[j + 1].isalpha():
            str2_list.append(str2[j:j + 2])

    Counter1 = Counter(str1_list)
    Counter2 = Counter(str2_list)
    print("Counter1\n", Counter1)
    print("Counter2\n", Counter2)
    # 교집합
    inter = list((Counter1 & Counter2).elements())
    # 합집합
    union = list((Counter1 | Counter2).elements())
    print("inter\n", inter)
    print("union\n", union)

    if len(inter) == 0 and len(union) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)

"""
def solution(str1,str2):
    list1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    list2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    tlist = set(list1)|set(list2) #
    res1 = [] # 합집합
    res2 = [] # 교집합
    if tlist: #값이 존재한다면
        for i in tlist:
            res1.extend([i]*max(list1.count(i),list2.count(i)))
            res2.extend([i]*min(list1.count(i),list2.count(i)))
            
        answer = int(len(res2)/len(res1)*65536)
        return answer
    else :
    return 65536


"""