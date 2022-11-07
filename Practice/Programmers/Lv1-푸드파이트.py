# https://school.programmers.co.kr/learn/courses/30/lessons/134240


def solution(food):
    foods = list()
    for i in range(len(food)):
        if len(food) <= 1:
            continue
        foods.extend([str(i)] * (food[i] // 2))

    return "".join(foods) + "0" + "".join(list(reversed(foods)))
