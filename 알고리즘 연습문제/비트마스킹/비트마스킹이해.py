switch_states = [True,False,False,True,True,False,False,True, True]
switch_states = 0b100110011 # 이처럼 표현 가능

"""
왜 비트마스크를 사용하는가?
    # 비트연산을 통한 삽입, 삭제, 조회 등이 간단해짐
    # 더 간결한 코드 작성이 가능
    # 더 빠른 연산이 가능
    # 비트마스크를 이용한 정수 표현으로 다이나믹 프로그래밍이 가능함. (중요)
    

"""

#원소 추가
n = 3
print(bin(0b0010 | (1 << n)))  #  0b1010
#원소 제거
n = 3
print(bin(0b1010 & ~(1 << n)))  #  0b10
#원소 조회
n = 3
print(bin(0b1010 & (1 << n)))  #  0b1000
#원소 토글 (XOR)
n = 3
print(bin(0b1010 ^ (1 << n)))  #  0b10