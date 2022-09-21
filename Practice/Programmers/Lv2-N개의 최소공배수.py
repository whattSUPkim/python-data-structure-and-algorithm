# https://school.programmers.co.kr/learn/courses/30/lessons/12953
from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


def solution(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result = lcm(result, arr[i])
    return result
