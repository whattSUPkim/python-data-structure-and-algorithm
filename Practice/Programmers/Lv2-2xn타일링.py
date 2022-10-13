# https://school.programmers.co.kr/learn/courses/30/lessons/12900
def solution(n):
    cache = [0 for _ in range(n + 1)]
    cache[1] = 1
    cache[2] = 2
    for i in range(3, n + 1):
        cache[i] = (cache[i - 2] + cache[i - 1]) % 1000000007

    return cache[n]


"""
n = 1 
1
n = 2 
11
2
n = 3 
111
12
21
n = 4
1111
112
121
211
22
"""
