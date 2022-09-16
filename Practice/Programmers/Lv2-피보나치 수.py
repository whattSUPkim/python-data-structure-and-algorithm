# https://school.programmers.co.kr/learn/courses/30/lessons/12945
def solution(n):
    cache = [0 for _ in range(n + 1)]
    cache[1] = 1
    for i in range(2, len(cache)):
        cache[i] = cache[i - 2] + cache[i - 1]

    return cache[n] % 1234567
