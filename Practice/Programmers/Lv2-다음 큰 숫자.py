# https://school.programmers.co.kr/learn/courses/30/lessons/12911


def solution(n):
    n_bin = bin(n).count("1")
    candidate = n
    while True:
        candidate += 1
        if bin(candidate).count("1") == n_bin:
            return candidate
