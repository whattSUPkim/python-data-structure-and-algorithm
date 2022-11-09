# https://school.programmers.co.kr/learn/courses/30/lessons/12946
# 해설 찾아보고, 다음 날 재풀이


def solution(n):
    global answer
    answer = []
    hanoi(n, 1, 2, 3)

    return answer


def hanoi(n, start, mid, end):
    if n == 1:
        answer.append([start, end])
        return

    hanoi(n - 1, start, end, mid)
    answer.append([start, end])
    hanoi(n - 1, mid, start, end)


if solution(2) == [[1, 2], [1, 3], [2, 3]]:
    print("통과")
print(solution(4))

"""
[321][][]
[32][][1]
[3][2][1]
[3][21][]
[][21][3]
[1][2][3]
[1][][32]
[][][321]
"""
