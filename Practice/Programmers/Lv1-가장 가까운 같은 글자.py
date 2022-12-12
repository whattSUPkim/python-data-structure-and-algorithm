# https://school.programmers.co.kr/learn/courses/30/lessons/142086


def solution(s):
    answer = []
    d = dict()
    for i in range(len(s)):
        if d.get(s[i], i) == i:
            answer.append(-1)
            d[s[i]] = i
        else:
            answer.append(i - d[s[i]])
            d[s[i]] = i

    return answer
