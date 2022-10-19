# https://school.programmers.co.kr/learn/courses/30/lessons/68936


def compress_square(square):
    half = len(square) // 2
    s1, s2, s3, s4 = [], [], [], []
    for i in range(half):
        s1.extend([square[i][0:half]])
        s2.extend([square[i][half:]])
    for i in range(half, len(square)):
        s3.extend([square[i][0:half]])
        s4.extend([square[i][half:]])
    for s in [s1, s2, s3, s4]:
        checker = sum(sum(s, []))
        if checker == 0:
            answer[0] += 1
        elif checker == len(s) ** 2:
            answer[1] += 1
        else:
            compress_square(s)


def solution(arr):
    checker = sum(sum(arr, []))
    if checker == 0:
        return [1, 0]
    if checker == len(arr) ** 2:
        return [0, 1]

    global answer
    answer = [0, 0]
    compress_square(arr)
    return answer
