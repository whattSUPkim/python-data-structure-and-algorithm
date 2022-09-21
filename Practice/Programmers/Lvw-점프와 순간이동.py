# https://school.programmers.co.kr/learn/courses/30/lessons/12980
def solution(n):
    usage = 0
    while n > 0:
        if n % 2 != 0:
            n -= 1
            usage += 1
        n //= 2

    return usage
