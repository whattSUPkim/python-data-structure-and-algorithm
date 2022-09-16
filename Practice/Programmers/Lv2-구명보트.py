# https://school.programmers.co.kr/learn/courses/30/lessons/42885
from collections import deque


def solution(people, limit):
    answer = 0
    queue = deque(sorted(people, reverse=True))
    while queue:
        num = queue.popleft()
        answer += 1
        try:
            while True:
                if num + queue[-1] > limit:
                    break
                num += queue.pop()
        except:
            break

    return answer
