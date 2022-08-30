# https://school.programmers.co.kr/learn/courses/30/lessons/118667
from collections import deque


def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    answer = 0

    for _ in range((len(queue1) + len(queue2)) * 2):
        if sum1 == sum2:
            return answer
        elif sum1 > sum2:
            temp = queue1.popleft()
            queue2.append(temp)
            sum1 -= temp
            sum2 += temp
        else:
            temp = queue2.popleft()
            queue1.append(temp)
            sum2 -= temp
            sum1 += temp
        answer += 1
    return -1
