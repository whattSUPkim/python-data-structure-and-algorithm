# https://school.programmers.co.kr/learn/courses/30/lessons/87390
"""
123 223 333
1234 2234 3334 4444
12345 22345 33345 44445 55555
"""


def solution(n, left, right):
    arr = []
    start = left // n + 1
    end = right // n + 1
    for i in range(start, end + 1):
        tmp1 = [i] * (i - 1)
        tmp2 = [j for j in range(i, n + 1)]
        arr.extend(tmp1)
        arr.extend(tmp2)

    result_left = left % n
    result_right = n - (right % n + 1)
    if result_right == 0:
        return arr[result_left:]
    else:
        return arr[result_left:-result_right]
