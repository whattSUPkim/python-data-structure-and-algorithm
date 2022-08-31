# https://school.programmers.co.kr/learn/courses/30/lessons/12914
def solution(n):
    cache = [0 for _ in range(n+1)]
    cache[0] = 1
    cache[1] = 1
    
    for i in range(2, len(cache)):
        cache[i] = cache[i-2] + cache[i-1]
    
    return cache[n] % 1234567
'''
# 1
1
# 2
11
2
# 3
111
21
12
# 4
1111
211
121
112
22
# 5
11111
2111
1211
1121
1112
221
212
112
-> i-2의 경우의 수에 2를 추가 + i-1 경우의 수에 1을 추가
'''

