# https://school.programmers.co.kr/learn/courses/30/lessons/49993#


def solution(skill, skill_trees):
    possible_skill_sets = {skill[:i] for i in range(len(skill) + 1)}
    answer = 0
    skill = set(skill)
    for skills in skill_trees:
        tmp = ""
        for s in skills:
            if s in set(skill):
                tmp += s
        if tmp in possible_skill_sets:
            answer += 1

    return answer
