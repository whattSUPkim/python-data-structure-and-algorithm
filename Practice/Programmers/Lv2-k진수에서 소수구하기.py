# https://school.programmers.co.kr/learn/courses/30/lessons/92335
import math


def is_prime(n):
    """n이 소수인지를 판단합니다."""
    if n <= 1:
        return 0

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1


def converter(n, k):
    """n을 k진수로 변환합니다."""
    tmp = ""
    while n:
        tmp += str(n % k)
        n = n // k  #

    return tmp[::-1]


def solution(n, k):
    answer = 0

    nums = converter(n, k).split("0")
    for n in nums:
        if n != "":
            answer += is_prime(int(n))

    return answer
