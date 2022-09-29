# https://school.programmers.co.kr/learn/courses/30/lessons/42584#
from collections import deque


def solution(prices):
    answer = [_ for _ in range(len(prices) - 1, -1, -1)]
    stack = [0]
    for i in range(1, len(prices)):
        while True:
            if not stack or prices[stack[-1]] <= prices[i]:
                stack.append(i)
                break
            stack_idx = stack.pop()
            answer[stack_idx] = i - stack_idx

    return answer
