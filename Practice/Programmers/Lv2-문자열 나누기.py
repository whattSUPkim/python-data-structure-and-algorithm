# https://school.programmers.co.kr/learn/courses/30/lessons/140108


def solution(strings):
    answer = 0
    tmp = [None, 0, 0]
    for s in strings:
        if not tmp[0]:
            tmp[0] = s
            tmp[1] += 1
            continue
        if s == tmp[0]:
            tmp[1] += 1
        else:
            tmp[2] += 1

        if tmp[1] != 0 and tmp[1] == tmp[2]:
            answer += 1
            tmp = [None, 0, 0]

    if tmp[1] + tmp[2] != 0:
        answer += 1

    return answer
