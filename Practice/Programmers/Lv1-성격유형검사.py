# https://school.programmers.co.kr/learn/courses/30/lessons/118666?language=python3
def solution(survey, choices):
    answer = ""
    table_name = ["RT", "CF", "JM", "AN"]
    table = {name: 0 for name in table_name}

    for i in range(len(survey)):
        s = survey[i]
        c = choices[i] - 4
        try:
            table[s] += c
        except:
            table[s[::-1]] += -c

    for name in table_name:
        if table[name] <= 0:
            answer += name[0]
        else:
            answer += name[1]

    return answer

