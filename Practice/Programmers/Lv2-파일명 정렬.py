# https://school.programmers.co.kr/learn/courses/30/lessons/17686
import re


def solution(files):
    sorting_list = list()
    for i in range(len(files)):
        file = files[i]
        start, end = re.search("[0-9]+", file).span()
        head = file[:start]
        number = file[start:end]
        sorting_list.append([head.lower(), int(number), i])

    answer = list()
    for l in sorted(sorting_list, key=lambda x: (x[0], x[1], x[2])):
        answer.append(files[l[2]])
    return answer
