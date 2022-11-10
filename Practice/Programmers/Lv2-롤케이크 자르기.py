# https://school.programmers.co.kr/learn/courses/30/lessons/132265
def solution(topping):
    answer = 0
    n = len(set(topping))
    left = [[0 for _ in range(10001)], 0]
    right = [[[] for _ in range(10001)], n]
    for t in topping:
        right[0][t].append(1)
    n //= 2

    for t in topping:
        right[0][t].pop()
        if len(right[0][t]) == 0:
            right[1] -= 1
        if left[0][t] == 0:
            left[1] += 1
            left[0][t] = 1
        if left[1] == right[1]:
            answer += 1

    return answer


"""
# 뺼 때 비는지 검사 / 넣을 때 새롭게 추가되는 지 검사

[1][][][]
[1][1][1][1]
"""
