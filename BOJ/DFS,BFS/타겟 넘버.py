# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3
# 타겟넘버

answer = 0


def dfs(numbers, sum_value, target, index):
    global answer
    if index == len(numbers):
        if sum_value == target:
            answer += 1
        return
    dfs(numbers, sum_value + numbers[index], target, index + 1) # 재귀함수로 2개부호 둘다 돌리기
    dfs(numbers, sum_value - numbers[index], target, index + 1)


def solution(numbers, target):
    dfs(numbers, 0, target, 0)
    return answer

numbers = [1,1,1,1,1]
target = 3
print(solution(numbers,target))