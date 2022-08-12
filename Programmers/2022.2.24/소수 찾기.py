# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3
"""

문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

"""

from itertools import permutations

def is_prime(n) :
    if n== 0 or n ==1 : return False
    # 소수임을 증명하는법 : 제곱근들로 나눠지지 않는다면 소수
    for i in range(2,int(n**0.5)+ 1 ) :
        if n%i == 0 :
            return False
    return True

def solution(numbers) :
    answer = 0
    lst = [number for number in numbers]
    set_number = set()

    for i in range(1,len(numbers)+1) :
        # 완전탐색이므로, permutations 모듈 사용
        candidates = permutations(lst,i)
        for candidate in candidates :
            # 해당 쪼개진 문자를 합쳐서 set에 넣고,
            cur = ''.join(candidate)
            set_number.add(cur)

    for number in set_number :
        #소수라면, answer ++
        if is_prime(number) :
            answer +=1
    return answer

