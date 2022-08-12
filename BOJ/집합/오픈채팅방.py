# Programmers https://programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    answer = []
    dic = {} #딕셔너리 생성

    for sentence in record:
        sentence_split = sentence.split()
        # 맨 첫단어가 Enter or Change 일경우만
        if sentence_split[0] == 'Enter' or sentence_split[0] == 'Change':
            dic[sentence_split[1]] = sentence_split[2]

    for sentence in record:
        sentence_split = sentence.split()
        if sentence_split[0] == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(dic[sentence_split[1]]))
        if sentence_split[0] == 'Leave':
            answer.append("{}님이 나갔습니다.".format(dic[sentence_split[1]]))
    return answer

#record testcase
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))