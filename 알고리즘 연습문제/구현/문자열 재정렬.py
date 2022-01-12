"""
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다.
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한값을 이어서 출력
ex) K1KA5CB7 -> ABCKK13

"""

n = input()
lst = []
sumOfNumber = 0
for i in range(len(n)):
    if n[i].isalpha():
        lst.append(n[i])
    else :
        sumOfNumber += int(n[i])

lst.sort()
result = "".join(lst)
result +=str(sumOfNumber)
print(result)