# https://school.programmers.co.kr/learn/courses/30/lessons/17680
from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    answer = 0
    cache = deque()
    for c in cities:
        c = c.lower()
        if c in cache:
            cache.remove(c)
            cache.append(c)
            answer += 1
        else:
            cache.append(c)
            answer += 5
            if len(cache) > cacheSize:
                cache.popleft()

    return answer
